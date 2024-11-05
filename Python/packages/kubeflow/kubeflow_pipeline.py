# python 3.9
import os, pathlib, configparser, importlib
os.chdir( pathlib.Path(__file__).parent.resolve() )
# pip install kfp=1.8.3 # k8s 1.20 + kubeflow 1.6
from kfp.components import create_component_from_func as ccff
import kfp.dsl as dsl
import kfp

class createStep:
    def __init__(self, stepName, module):
        self.cfg = self.config2Dict(stepName)
        self.comp = ccff( getattr(module,stepName), base_image=self.cfg["base_image"])
    def config2Dict(self, stepName):
        cfg = configparser.ConfigParser()
        cfg.read(f"steps/{stepName}.cfg")
        return dict(cfg["default"])

def insert():
    with open("pipeline_yaml/pipeline.yaml", "r") as f:
    	L = f.readlines()
    insertIndices = [ i+1 for i in range(len(L)) if "image:" in L[i] ]
    for i in range(len(insertIndices)):
        insertIndices[i]+=i*10
        L.insert(insertIndices[i]+0, "      imagePullPolicy: Never\n")
        L.insert(insertIndices[i]+1, "      volumeMounts:\n")
        L.insert(insertIndices[i]+2, "      - name: pipelinevolume\n")
        L.insert(insertIndices[i]+3, "        mountPath: \"/nfs\"\n")
        L.insert(insertIndices[i]+4, "    hostNetwork: true\n") 
        L.insert(insertIndices[i]+5, "    volumes:\n")
        L.insert(insertIndices[i]+6, "      - name: pipelinevolume\n")
        L.insert(insertIndices[i]+7, "        nfs:\n")
        L.insert(insertIndices[i]+8, f"          server: {pcfg['host']}\n")
        L.insert(insertIndices[i]+9, f"          path: {pcfg['path']}\n")
    with open("pipeline_yaml/pipeline1.yaml", "w") as f:
        for line in L:
            f.write(line)

pcfg = configparser.ConfigParser()
pcfg.read("pipeline.cfg")
pcfg = dict(pcfg["default"])

moduleList = [ (stepName,importlib.import_module("steps."+stepName)) for stepName in pcfg["pipeline"].split(",") ]
stepList=[ createStep(stepName,module) for stepName,module in moduleList ]

@dsl.pipeline(name='PAUT', description='Auto packing')
def pipelinePaut(val:int):
    #taskDownload = stepList[0].comp(val, stepList[0].cfg)
    #taskExtract = stepList[1].comp(taskDownload.output, stepList[1].cfg)
    #taskCleaning = stepList[2].comp(taskExtract.output, stepList[2].cfg)
    #taskInference = stepList[3].comp(taskCleaning.output, stepList[3].cfg)
    #taskKeypoint = stepList[4].comp(taskInference.output, stepList[4].cfg)
    taskReport = stepList[5].comp(val, stepList[5].cfg)

kfp.compiler.Compiler().compile(pipelinePaut, "pipeline_yaml/pipeline.yaml")
insert()
client = kfp.Client("http://127.0.0.1:8080")
client.create_run_from_pipeline_package("pipeline_yaml/pipeline1.yaml", arguments={"val":0})
