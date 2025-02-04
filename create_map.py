def create_map(locations):
    """Cria mapa interativo com múltiplos pontos"""
    if not locations:
        return None
    
    try:
        # Centro do mapa baseado na média das coordenadas
        center_lat = sum(loc['lat'] for loc in locations) / len(locations)
        center_lon = sum(loc['lon'] for loc in locations) / len(locations)
        
        # Criar mapa base
        m = folium.Map(location=[center_lat, center_lon], zoom_start=11)
        
        try:
            # Tentar criar cluster de marcadores
            marker_cluster = folium.plugins.MarkerCluster(name="CEPs").add_to(m)
        except Exception as e:
            print(f"Erro ao criar cluster: {e}")
            # Se falhar, usar marcadores individuais sem cluster
            marker_cluster = m
        
        # Cores para os marcadores
        colors = ['red', 'blue', 'green', 'purple', 'orange', 'darkred', 
                 'darkblue', 'darkgreen']
        
        for i, loc in enumerate(locations):
            # Alterna cores
            color = colors[i % len(colors)]
            
            # HTML personalizado para popup
            popup_html = f"""
                <div style="width: 200px;">
                    <h4>CEP: {loc['cep']}</h4>
                    <p><b>Logradouro:</b> {loc['logradouro']}</p>
                    <p><b>Bairro:</b> {loc['bairro']}</p>
                    <p><b>Cidade/UF:</b> {loc['cidade']}-{loc['uf']}</p>
                    <p><b>Complemento:</b> {loc.get('complemento', 'N/A')}</p>
                </div>
            """
            
            try:
                # Adiciona marcador
                folium.Marker(
                    location=[loc['lat'], loc['lon']],
                    popup=folium.Popup(popup_html, max_width=300),
                    tooltip=f"CEP: {loc['cep']}",
                    icon=folium.Icon(color=color, icon='info-sign')
                ).add_to(marker_cluster)
            except Exception as e:
                print(f"Erro ao adicionar marcador: {e}")
                continue
        
        # Adiciona controle de camadas
        folium.LayerControl().add_to(m)
        
        # Ajusta visualização para incluir todos os pontos
        if locations:
            bounds = [[loc['lat'], loc['lon']] for loc in locations]
            m.fit_bounds(bounds)
        
        return m
        
    except Exception as e:
        print(f"Erro ao criar mapa: {e}")
        return None