
from flask import Flask, render_template
from pivottablejs import pivot_ui
from IPython.display import HTML
import pandas as pd
import os
from werkzeug.utils import secure_filename
app = Flask(__name__)

	
from flask import Flask, render_template, request, session
import pandas as pd
import os
from werkzeug.utils import secure_filename


app = Flask(__name__)

# Upload folder
UPLOAD_FOLDER = 'media/'
# Define allowed files (for this example I want only csv file)
ALLOWED_EXTENSIONS = {'csv'}
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER


@app.route('/',methods=("GET", "POST"))
def index():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
            # set the file path
            uploaded_file.save(file_path)
        df=pd.read_csv(file_path)
        pivot_ui(df, outfile_path='templates/pivottablejs.html')
        # HTML('templates/pivottablejs.html')
        return render_template('pivottablejs.html')
    # return 'test'
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)