# Neon Duckies -- Yuqing Wu, Sophie Liu, Hebe Huang
# SoftDev
# K13 - Template for Success
# 2021-10-08



import random
from flask import Flask, render_template

app = Flask(__name__);

@app.route("/")
def hello_world():


    #html = "<h2> Neon Duckies -- Yuqing Wu, Sophie Liu, Hebe Huang </h2><hr>";

    #html += "Random Weighted Job: " + (random.choices(list(dictionary), weights=dictionary.values()))[0] + "<br><br><br>";

    #html += "<table> <tr> <th> Job </th> <th> Percentage </th> </tr>";
    #for i in list(dictionary):
    #    html += "<tr>";
    #    html += ("<td>" + i + "&nbsp;&nbsp;&nbsp;</td>");
    #    html += ("<td>" + str(dictionary[i]) + "% </td>");
    #    html += "</tr>";
    return ""


@app.route("/occupyflaskst")
def test_tmplt():
    file = open("data/occupations.csv");
    lines = file.read().split("\n");
    del lines[0]; #Remove "Job Class, Percentage" line
    split = [];
    for i in lines:
        if "," in i:
            #remove quotes, split string into job and %, then convert % to float
            i = i.replace("\"","");
            comma = i.rsplit(",",1);
            comma[1] = float(comma[1]);
            #add to necessary arrays
            split.append(comma);

    del split[len(split)-1]; # Remove "Total" as a job
    dictionary = dict(split)
    job = (random.choices(list(dictionary), weights=dictionary.values()))[0]

    return render_template( 'tablified.html', foo="random occupation", random_job = job, collection=dictionary)


app.debug = True;
app.run()
