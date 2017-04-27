# coding:utf-8
#!/user/bin/python

from flask import Flask, render_template, Blueprint
from config.constants import staticFolder, templateFolder
from app.myapp import register_blue

app = Flask(__name__)
app.static_folder = staticFolder
app.template_folder = templateFolder




def main():
    config = {
        'host': '0.0.0.0',
        'port': 5001,
        'debug': True
    }
    register_blue(app)
    app.run(**config)


if __name__ == '__main__':
    main()