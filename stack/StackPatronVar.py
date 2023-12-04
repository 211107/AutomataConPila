import re

class StackPatronVar:
    def __init__(self):
        self.stack = []
        self.stopWord = ""
        self.tripAnalysis = []
        self.tripAnalysisError = []
        
    def clearData(self):
        self.stack = []
        self.stopWord = ""
        self.tripAnalysis = []
        self.tripAnalysisError = []
        

    def transition(self, estado, text):
        
        if(estado == "q_rechazo"):
            return "q_rechazo"
                 
        if estado == "q0" and text == 'var':
            self.stack.append(text)
            self.tripAnalysis.append("VX")
            self.tripAnalysis.append("var X")
            self.tripAnalysis.append("X")
            self.tripAnalysis.append("ID T")
            self.tripAnalysis.append("ID")
            self.tripAnalysis.append("LR T")
            self.tripAnalysis.append("LR")
            self.tripAnalysis.append("LR|NR|∈ T")
            self.tripAnalysis.append("T")
            self.tripAnalysis.append("int")
            return "q1"      
        else:           
            self.stopWord = text
    
        if estado == "q1":            
            if re.match("^[a-z0-9]+$", text):
                self.stack.append(text)
                self.tripAnalysis.append("a-z R T")
                self.tripAnalysis.append("R T")
                return "q2"
            else:
                self.stopWord = text
                return "q_rechazo"
        else:
            self.stopWord = text
                        
        if estado == "q2" and text == 'int':
            self.stack.append(text)
            self.tripAnalysis.append("T")
            self.tripAnalysis.append("int")            
            return "q_accept"             
        else:
            self.stopWord = text      
                
            
        return "q_rechazo"

    def validateInput(self, lineCode):
        actualState = "q0"
        lineCode = re.sub(' +', ' ', lineCode).strip()
        text = lineCode.split(" ");        
        for item in text:                    
            actualState = self.transition(actualState, item)

        return actualState == "q_accept"

    def getStack(self):
        return self.stack
    
    def getTripAnalysis(self):
        return self.tripAnalysis
    
    def getTripAnalysisError(self):        
        return self.tripAnalysisError
    
    def getStopWord(self):
        return f"Error en: {self.stopWord}"

