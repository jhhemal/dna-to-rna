from flask import Flask, render_template, redirect, url_for
from forms import DNAForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '062542c9096d1ba170772358976aba15'

@app.route('/', methods=['GET','POST'])
def home():
    form = DNAForm()
    rna = None
    dna = None
    dnalist = []
    derror = None
    notdnas = ['B', 'D', 'E', 'F', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'U', 'V', 'W', 'X', 'Y', 'Z']
    if form.validate_on_submit():
        dna = form.dna.data.upper()
        for notdna in notdnas:
            if notdna in dna :
                derror = "DNA doesn't contain other than A,C,T,G"
        # nonlocal dna
        rnadata = dna.maketrans('ACGT','UGCA')
        rna = dna.translate(rnadata)
        dnalist = [
            {'A' : dna.count('A')},
            {'C' : dna.count('C')},
            {'G' : dna.count('G')},
            {'T' : dna.count('T')},
            ]
        # if you don't want the form to be filled with previous data
        form.dna.data = ''

    return render_template('index.html', form=form, rna = rna, dna=dna, dlists=dnalist, derror=derror)

# @app.route('/rna', methods=['GET', 'POST'])
# def toRna():
#     return render_template('rna.html', rna=rna)


if __name__ == '__main__':
    app.run(debug=True)