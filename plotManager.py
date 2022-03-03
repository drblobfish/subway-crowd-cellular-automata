import IPython.display

class PLOTMANAGER():
    def __init__(self):
        self.wallColor = ["white","grey"]
        pass
    
    def plotNb(self,model):

        html = f'<svg width="{20*model.m}" height="{20*model.n}">'
        for i in range(model.m):
            for j in range(model.n):
                html += f'<rect x="{20*i}" y="{20*j}" width="{20}" height="{20}" style="fill:{self.wallColor[model.walls[j,i]]};stroke:black" />'
        
        for restcell in model.restCells:
            html += f'<rect x="{restcell.pos[1] * 20 + 2}" y="{restcell.pos[0] * 20 + 2}" width="{16}" height="{16}" style="fill:green;stroke:green" />'
        
        for agent in model.agents:
            html += f'<circle cx="{agent.pos[1] *20 + 10 }" cy="{agent.pos[0] *20 + 10 }" r="8" fill="red" />'
        html += '</svg>'

        chart = IPython.display.HTML(html)
        IPython.display.display(chart)
    
    def clear(self):
        IPython.display.clear_output()