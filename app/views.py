from flask import Flask, render_template

app = Flask(__name__)

@app.route('/projects')
def projects():
    projects = [
        {
            'name': 'GoPass',
            'description': 'GoPass es una plataforma web EvenTech diseñada para mitigar la reventa de entradas falsas en eventos deportivos en Argentina',
            'technologies': 'C#, .Net, SQLServer, React, Tailwindcss, Axios, Redux',
            'role': 'QA Tester',
            'image_url': '/static/img/GoPass.jpg',
            'github_url': 'https://github.com/CarlosDaniel661/Testing/tree/main/Casos%20de%20Prueba%20GoPass',
            'live_demo_url': 'https://www.youtube.com/watch?v=tBhVak_qkyc&t=3762s'
        },
        {
            'name': 'Bariló',
            'description': 'Es una plataforma web/app TravelTech pensada para que los estudiantes y grupos de padres puedan organizar el viaje de egresados de ensueños, facilitando la selección de hospedajes y tours o actividades a realizar durante la excursión.',
            'technologies': 'Java 17, Spring Boot 3, Maven, Spring Security, JUnit + Mockito, React, Tailwindcss, TypeScript',
            'role': 'QA Tester',
            'image_url': '/static/img/Bariló.jpg',
            'github_url': 'https://github.com/CarlosDaniel661/Testing/tree/main/Casos%20de%20Prueba%20Baril%C3%B3',
            'live_demo_url': 'https://www.youtube.com/watch?v=qqw0mvAC-EQ&t=2217s'
        },
        {
            'name': 'Reffindr',
            'description': 'Reffindr es una plataforma web PropTech creada para simplificar el alquiler de propiedades, beneficiando a inquilinos y propietarios',
            'technologies': 'C#, .NET, Python, Azure Storage, SQLite, Nodejs, Render, Docker',
            'role': 'QA Tester Lead',
            'image_url': '/static/img/Carátula Reffindr.jpg',
            'github_url': 'https://github.com/CarlosDaniel661/Testing/tree/main/Casos%20de%20Prueba%20Reffindr',
            'live_demo_url': 'https://www.youtube.com/watch?v=R47FG1XkoVQ&t=2705s'
        }
    ]
    return render_template('projects.html', projects=projects)

if __name__ == '__main__':
    app.run(debug=True)