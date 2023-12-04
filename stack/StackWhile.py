import re

class StackWhile:
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
        
        if estado == "q_rechazo":                        
            return "q_rechazo" 
        
        if estado == "q0" and text == 'mientras':
            self.stack.append(text)           
            self.tripAnalysis.append("SC3")
            self.tripAnalysis.append("mientras C3")
            self.tripAnalysis.append("C3")
            self.tripAnalysis.append("C2 Lc")
            self.tripAnalysis.append("C2")
            self.tripAnalysis.append("C1 R")
            self.tripAnalysis.append("C1")            
            return "q1" 
        else:
            self.stopWord = text          
            
        
        if estado == "q1" and (text == 'verdadero{' ):                            
            self.tripAnalysis.append("n LA")
            self.tripAnalysis.append("verdadero { R")
            self.tripAnalysis.append("R")
            self.tripAnalysis.append("MR|mR|NR|∈ LC")
            self.tripAnalysis.append("LC")
            self.tripAnalysis.append("}")            
            return "q_accept"              
        else:
            self.stopWord = text                            
        
    def validateInput(self, input):
        actualState = "q0"
        input = re.sub(' +', ' ', input).strip()
        text = input.split(" ");        
        for word in text:            
            actualState = self.transition(actualState, word)

        return actualState == "q_accept"

    def getStack(self):
        return self.stack
    
    def getTripAnalysis(self):
        return self.tripAnalysis
    
    def getTripAnalysisError(self):        
        return self.tripAnalysisError
     
    def getStopWord(self):
        return f"Error en: {self.stopWord}"

  