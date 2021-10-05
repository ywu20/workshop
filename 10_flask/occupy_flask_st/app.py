# Team Polar: Yuqing Wu, Jesse Xie, Rachel Xiao
# SoftDev
# K10 -- Putting Little Pieces Together
# 2021-10-04
import K06
from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    keys = ""
    print("the __name__ of this module is... ")
    print(__name__)
    heading = '''Team Polar: Yuqing Wu, Jesse Xie, Rachel Xiao <br/>
    SoftDev <br/>
    K10 -- Putting Little Pieces Together<br/>
    2021-10-04 <br/><br/>'''

#apparently the problem goes away if we use dictionary.keys() instead of a list
    return ""+heading+K06.main() + "<br/>\n<br/>"+str(K06.occupations.keys())

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
