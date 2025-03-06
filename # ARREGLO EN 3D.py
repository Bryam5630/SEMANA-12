# Crear matriz 3D para temperaturas (incluso por semanas)
TEMPERATURAS = [
    # PUYO
    [
        # Semana 1
        [
            ["Lunes", 15],
            ["Martes", 20],
            ["Miércoles", 21],
            ["Jueves", 26],
            ["Viernes", 17],
            ["Sábado", 22],
            ["Domingo", 16]
        ],
        # Semana 2
        [
            ["Lunes", 14],
            ["Martes", 19],
            ["Miércoles", 20],
            ["Jueves", 25],
            ["Viernes", 18],
            ["Sábado", 21],
            ["Domingo", 17]
        ],
        # Semana 3
        [
            ["Lunes", 13],
            ["Martes", 18],
            ["Miércoles", 19],
            ["Jueves", 22],
            ["Viernes", 16],
            ["Sábado", 23],
            ["Domingo", 15]
        ],
        # Semana 4
        [
            ["Lunes", 16],
            ["Martes", 21],
            ["Miércoles", 22],
            ["Jueves", 27],
            ["Viernes", 19],
            ["Sábado", 24],
            ["Domingo", 18]
        ]
    ],

    # QUITO
    [
        # Semana 1
        [
            ["Lunes", 10],
            ["Martes", 12],
            ["Miércoles", 11],
            ["Jueves", 13],
            ["Viernes", 14],
            ["Sábado", 15],
            ["Domingo", 9]
        ],
        # Semana 2
        [
            ["Lunes", 12],
            ["Martes", 13],
            ["Miércoles", 14],
            ["Jueves", 15],
            ["Viernes", 16],
            ["Sábado", 17],
            ["Domingo", 10]
        ],
        # Semana 3
        [
            ["Lunes", 13],
            ["Martes", 14],
            ["Miércoles", 15],
            ["Jueves", 16],
            ["Viernes", 17],
            ["Sábado", 18],
            ["Domingo", 11]
        ],
        # Semana 4
        [
            ["Lunes", 14],
            ["Martes", 15],
            ["Miércoles", 16],
            ["Jueves", 17],
            ["Viernes", 18],
            ["Sábado", 19],
            ["Domingo", 12]
        ]
    ],

    # TULCÁN
    [
        # Semana 1
        [
            ["Lunes", 8],
            ["Martes", 9],
            ["Miércoles", 10],
            ["Jueves", 11],
            ["Viernes", 12],
            ["Sábado", 13],
            ["Domingo", 7]
        ],
        # Semana 2
        [
            ["Lunes", 9],
            ["Martes", 10],
            ["Miércoles", 11],
            ["Jueves", 12],
            ["Viernes", 13],
            ["Sábado", 14],
            ["Domingo", 8]
        ],
        # Semana 3
        [
            ["Lunes", 10],
            ["Martes", 11],
            ["Miércoles", 12],
            ["Jueves", 13],
            ["Viernes", 14],
            ["Sábado", 15],
            ["Domingo", 9]
        ],
        # Semana 4
        [
            ["Lunes", 11],
            ["Martes", 12],
            ["Miércoles", 13],
            ["Jueves", 14],
            ["Viernes", 15],
            ["Sábado", 16],
            ["Domingo", 10]
        ]
    ],

    # MACAS
    [
        # Semana 1
        [
            ["Lunes", 20],
            ["Martes", 23],
            ["Miércoles", 21],
            ["Jueves", 22],
            ["Viernes", 24],
            ["Sábado", 25],
            ["Domingo", 19]
        ],
        # Semana 2
        [
            ["Lunes", 21],
            ["Martes", 24],
            ["Miércoles", 22],
            ["Jueves", 23],
            ["Viernes", 25],
            ["Sábado", 26],
            ["Domingo", 20]
        ],
        # Semana 3
        [
            ["Lunes", 22],
            ["Martes", 25],
            ["Miércoles", 23],
            ["Jueves", 24],
            ["Viernes", 26],
            ["Sábado", 27],
            ["Domingo", 21]
        ],
        # Semana 4
        [
            ["Lunes", 23],
            ["Martes", 26],
            ["Miércoles", 24],
            ["Jueves", 25],
            ["Viernes", 27],
            ["Sábado", 28],
            ["Domingo", 22]
        ]
    ]
]

ciudades = ["Puyo", "Quito", "Tulcán", "Macas"]


for ciudad_index, ciudad in enumerate(TEMPERATURAS):
    print(f"\nPromedios de temperaturas en {ciudades[ciudad_index]}:")

    for semana_index, semana in enumerate(ciudad):
        total_temperaturas = 0  

        for dia in semana:
            total_temperaturas += dia[1] 
        
        promedio = total_temperaturas / 7
        
        print(f"Semana {semana_index + 1}: {promedio:.2f}°C")