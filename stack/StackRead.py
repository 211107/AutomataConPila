import re

class StackRead:
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

        if estado == "q0":            
            if (text == "leer"):                                
                self.tripAnalysis.append("LE LE1")
                self.tripAnalysis.append("leer LE1")
                self.tripAnalysis.append("LE1")
                self.tripAnalysis.append("PA LE2")                
                return "q1"
            else:                
                self.stopWord = text                
                return "q_rechazo"
        else:
            self.stopWord = text        
            
        if estado == "q1":            
            if (text == "("):       
                self.tripAnalysis.append("PA")
                self.tripAnalysis.append("( LE2")                        
                self.tripAnalysis.append("LE LE1")
                self.tripAnalysis.append("leer LE1")
                self.tripAnalysis.append("LE1")
                self.tripAnalysis.append("PA LE2")   
                return "q2"
            else:                
                self.stopWord = text                
                return "q_rechazo"
        else:
            self.stopWord = text                    

        if estado == "q2":            
            if (re.match('^[a-zA-Z0-9]+$', text)):     
                self.tripAnalysis.append("LE2")
                self.tripAnalysis.append("R PC")    
                self.tripAnalysis.append("R")
                self.tripAnalysis.append("MR|mR|NR PC")                                       
                self.stack.append(text)
                return "q3"
            else:                
                self.stopWord = text  
                self.tripAnalysis.append("LE2")
                self.tripAnalysis.append("R PC")    
                self.tripAnalysis.append("R")
                self.tripAnalysis.append("MR|mR|NR PC")               
                return "q_rechazo"
        else:
            self.stopWord = text

        if estado == "q3":            
            if (text == ")"):                                
                self.tripAnalysis.append("PC")
                self.tripAnalysis.append(")")                
                return "q_accept"
            else:                
                self.stopWord = text               
                return "q_rechazo"
        else:
            self.stopWord = text               
                   
        
        # if estado == "q1" and (text == 'verdadero' ):                            
        #     return "q_accept"              
        # else:
        #     self.stopWord = text   
             
        return "q_rechazo"        
        
    def validateInput(self, input):
        actualState = "q0"
        patron = re.compile(r'(([a-zA-Z]|[0-9])+|\(|\)(.*?))')

        # Obtener la lista de coincidencias
        text = [match[0] for match in patron.findall(input)]

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

