import re

class StackPatronFunction:
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
        
        if estado == "q0" and text == 'fun':
            self.tripAnalysis.append("F3LC")
            self.tripAnalysis.append("F3")
            self.tripAnalysis.append("F2 R")
            self.tripAnalysis.append("F2")
            self.tripAnalysis.append("F1 L1")
            self.tripAnalysis.append("F1")
            self.tripAnalysis.append("F P1")
            self.tripAnalysis.append("F")
            self.tripAnalysis.append("S R")
            self.tripAnalysis.append("S")
            self.tripAnalysis.append("fun R")                        
            return "q1" 
        else:        
            self.stopWord = text
      
        
        if estado == "q1" and re.match(r'[a-zA-Z0-9]*\([^ ]*\)\s*{', text):
            self.tripAnalysis.append("R")
            self.tripAnalysis.append("MR|mR|NR|∈ P1")
            self.tripAnalysis.append("P1")
            self.tripAnalysis.append("PA PC")
            self.tripAnalysis.append("( PC")
            self.tripAnalysis.append("PC")
            self.tripAnalysis.append(") LI")
            self.tripAnalysis.append("L1")
            self.tripAnalysis.append("LA R")
            self.tripAnalysis.append("LA")
            self.tripAnalysis.append("{ R")
            self.tripAnalysis.append("MR|mR|NR|∈ LC")                                         
            return "q_accept"                            
        else:
            self.stopWord = text                  
              
        
        if estado == "q2" and text == '{':             
            self.tripAnalysis.append("LC")
            self.tripAnalysis.append("}")               
            return "q_accept" 
        else:
            self.stopWord = text                       
        
        return "q_rechazo"
        
    def validateInput(self, input:str):
        actualState = "q0"
        text = []
        text = input.split(" ");    
        temp = []
        temp.append(text[0])   
        ppp = ""
        for item in text[1]:             
            ppp = ppp + item    
        temp.append(ppp)        
        for word in temp:            
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
