from flask import Blueprint, render_template

app = Blueprint('main', __name__)

@app.route('/')
def index():
    projects_data = [
        {
            'name': 'GoPass',
            'description': 'GoPass es una plataforma web EvenTech diseñada para mitigar la reventa de entradas falsas en eventos deportivos en Argentina',
            'technologies': 'C#, .Net, SQLServer, React, Tailwindcss, Axios, Redux',
            'role': 'QA Tester',
            'image_url': '/static/img/GoPass.jpg',
            'github_url': 'https://github.com/CarlosDaniel661/Testing/tree/main/Casos%20de%20Prueba%20GoPass',
            'live_demo_url': 'https://www.youtube.com/watch?v=tBhVak_qkyc&t=2323s'
        },
        {
            'name': 'Bariló',
            'description': 'Es una plataforma web/app TravelTech pensada para que los estudiantes y grupos de padres puedan organizar el viaje de egresados de ensueños, facilitando la selección de hospedajes y tours o actividades a realizar durante la excursión.',
            'technologies': 'Java 17, Spring Boot 3, Maven, Spring Security, JUnit + Mockito, React, Tailwindcss, TypeScript',
            'role': 'QA Tester',
            'image_url': '/static/img/Bariló.jpg',
            'github_url': 'https://github.com/CarlosDaniel661/Testing/tree/main/Casos%20de%20Prueba%20Baril%C3%B3',
            'live_demo_url': 'https://www.youtube.com/watch?v=qqw0mvAC-EQ&t=1762s'
        },
        {
            'name': 'Reffindr',
            'description': 'Reffindr es una plataforma web PropTech creada para simplificar el alquiler de propiedades, beneficiando a inquilinos y propietarios',
            'technologies': 'C#, .NET, Python, Azure Storage, SQLite, Nodejs, Render, Docker',
            'role': 'QA Tester Lead',
            'image_url': '/static/img/Carátula Reffindr.jpg',
            'github_url': 'https://github.com/CarlosDaniel661/Testing/tree/main/Casos%20de%20Prueba%20Reffindr',
            'live_demo_url': 'https://www.youtube.com/watch?v=R47FG1XkoVQ&t=1408s'
        }
    ]
    
    reconocimientos_data = [
        {
            'name': 'Introducción al Desarrollo 1',
            'description': 'Certificado de aprobación del curso de introducción al Desarrollo, utilizando HTML y CSS.',
            'image_url': '/static/img/Informatorio E1.jpg'
        },
        {
            'name': 'Desarrollo Web',
            'description': 'Certificado de una segunda etapa, donde se profundizó en el Desarrollo Web, utilizando Python, Django, conceptos de POO, Programación funcional y uso de base de datos relacionales.',
            'image_url': '/static/img/Informatorio E2.jpg'
        },
        {
            'name': 'Programación para el análisis de datos',
            'description': 'Un curso intensivo sobre el uso de Python para el análisis de datos.',
            'image_url': '/static/img/Python.jpg'
        },
        {
            'name': 'English for Developers',
            'description': 'Certificado de aprobación de un curso intensivo del idioma Inglés, enfocándose principalmente en lo necesario para la carrera en IT.',
            'image_url': '/static/img/English.jpg'
        },
        {
            'name': 'Certificado QA Tester',
            'description': 'Certificado de reconocimiento por la participación del Intake 003 de Igrowker, en donde apliqué todos los conocimientos adquiridos a lo largo de estos años.',
            'image_url': '/static/img/I003.jpg'
        },
        {
            'name': 'Certificado QA Tester Lead',
            'description': 'Reconocimento de una nueva participación en el Intake 004, esta vez ya desempeñando el rol de QA Tester Lead, en donde puse en práctica mi experiencia en liderazgo adquirido a lo largo de los años en cursos y trabajos anteriores, como así tambien todo lo aprendido en Testing de Software.',
            'image_url': '/static/img/Certificado QA Lead.jpg'
        },
        {
            'name': 'Certificado QA Tester',
            'description': 'Reconocimiento a la participación de un proyecto colaborativo FinTech en donde me desempeñé como QA Tester.',
            'image_url': '/static/img/NoCountry.jpg'
        },
        {
            'name': 'Certificado QA Tester',
            'description': 'Certificado de aprobación del curso de Testing de Software, completado en el Informatorio Chaco, una de mis puertas de entrada junto con otros cursos a los que me suscribí de manera autodidacta para ingresar al mundo IT.',
            'image_url': '/static/img/Certi testing.jpg'
        },
        {
            'name': 'Reconocimiento',
            'description': 'Reconocomiento al equipo de trabajo por su compañerismo y apoyo constante a otros equipos.',
            'image_url': '/static/img/ReconocimientoGoPass.jpg'
        }
    ]

    stacks_data = [
        {
            'image_url': '/static/img/github.png'
        },
        {
            'image_url': '/static/img/Java.png'
        },
        {
            'image_url': '/static/img/Jira.png'
        },
        {
            'image_url': '/static/img/Jmeter.png'
        },
        {
            'image_url': '/static/img/MySql.png'
        },
        {
            'image_url': '/static/img/postgresql.png'
        },
        {
            'image_url': '/static/img/Postman.png'
        },
        {
            'image_url': '/static/img/Python.png'
        },
        {
            'image_url': '/static/img/selenium.png'
        },
        {
            'image_url': '/static/img/SqlServer.png'
        },
        {
            'image_url': '/static/img/Notion.png'
        },
        {
            'image_url': '/static/img/cypress.png'
        }
    ]

    feedbacks_data = [
        {
            'image_url': '/static/img/Feed360.jpg'
        },
        {
           'image_url': '/static/img/FeedJP.jpg'
        },
        {
            'image_url': '/static/img/FeedPat.jpg'
        }
    ]
    
    return render_template('index.html', projects=projects_data, reconocimientos=reconocimientos_data, stacks=stacks_data, feedbacks=feedbacks_data)
