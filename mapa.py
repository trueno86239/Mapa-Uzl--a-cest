mapa = { 'A': [('B', 1, 'obousměrná')], 
        'B': [('A', 1, 'obousměrná'), ('C', 3, 'obousměrná'), ('D', 2, 'jednosměrná')],
        'C': [('B', 3, 'obousměrná'), ('E', 4, 'obousměrná')],
        'D': [('H', 3, 'obousměrná'), ('G', 2, 'obousměrná')],
        'E': [('F', 2, 'obousměrná'), ('C', 4, 'obousměrná')],
        'F': [('E', 2, 'obousměrná'), ('I', 3, 'obousměrná')],
        'G': [('D', 2, 'obousměrná')],
        'H': [('D', 3, 'obousměrná'), ('G', 2, 'jednosměrná'), ('F', 2, 'jednosměrná')],
        'I': [('F', 3, 'obousměrná')]
        }

for mesto, cesty in mapa.items():
        print(f"Město {mesto} má cesty: {cesty}")
