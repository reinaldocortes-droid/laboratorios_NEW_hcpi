from pathlib import Path
import pandas as pd
def resolver_ruta_archivo(nombre_archivo="air_quality_telemetry.csv") -> Path:
    candidatos = [
        Path("data") / nombre_archivo,
        Path("..") / "data" / nombre_archivo,
        Path("..") / ".." / "data" / nombre_archivo,
        Path("examples") / "data" / nombre_archivo,
    ]
    
    for ruta in candidatos:
        if ruta.exists():
            print(f"[OK] Archivo encontrado localmente en: {ruta.resolve()}")
            return ruta.resolve()
            
    print("[INFO] Archivo no encontrado localmente. Descargando dataset de respaldo...")
    url_fuente = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pollution.csv"
    ruta_destino = Path("data") / nombre_archivo
    ruta_destino.parent.mkdir(parents=True, exist_ok=True)
    
    import urllib.request
    urllib.request.urlretrieve(url_fuente, ruta_destino)
    print(f"[OK] Dataset descargado exitosamente en: {ruta_destino.resolve()}")
    return ruta_destino.resolve()

#hajaja
def auditar_calidad_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Genera una tabla de diagnóstico cuantitativo de calidad de datos por columna.
    """
    total_filas = len(df)
    conteo_nulos = df.isna().sum()
    porcentaje_nulos = (conteo_nulos / total_filas) * 100.0
    
    auditoria = pd.DataFrame({
        'Tipo de Dato': df.dtypes,
        'Valores No Nulos': df.notna().sum(),
        'Valores Nulos (NaN)': conteo_nulos,
        'Pérdida (%)': porcentaje_nulos.round(2),
        'Valores Únicos': df.nunique()
    })
    return auditoria

def resumen_memoria_dataframe(df: pd.DataFrame) -> None:
    """
    Imprime el uso total de memoria RAM del DataFrame.
    """
    uso_mb = df.memory_usage(deep=True).sum() / (1024 ** 2)
    print(f"Dimensiones: {df.shape[0]:,} filas x {df.shape[1]} columnas")
    print(f"Uso total estimado en memoria RAM: {uso_mb:.2f} MB")
    