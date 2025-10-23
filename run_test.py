import pytest
import subprocess
import sys
import os

def run_tests():
    """
    Función para ejecutar todas las pruebas con reporte HTML
    """
    print("Iniciando ejecucion de pruebas de automatizacion QA...")
    print("=" * 60)
    
    # Comando para ejecutar las pruebas con reporte HTML
    cmd = [
        "pytest", 
        "tests/", 
        "-v", 
        "--html=report.html", 
        "--self-contained-html",
        "--tb=short"
    ]
    
    try:
        # Ejecutar las pruebas
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        print("Resultados de las pruebas:")
        print(result.stdout)
        
        if result.stderr:
            print("Advertencias/Errores:")
            print(result.stderr)
        
        # Verificar si el reporte se generó correctamente
        if os.path.exists("report.html"):
            print("Reporte HTML generado exitosamente: report.html")
        else:
            print("No se pudo generar el reporte HTML")
            
        return result.returncode == 0
        
    except FileNotFoundError:
        print("Error: pytest no esta instalado. Instalalo con: pip install pytest pytest-html")
        return False
    except Exception as e:
        print(f"Error ejecutando las pruebas: {e}")
        return False

if __name__ == "__main__":
    success = run_tests()
    if success:
        print("\nTodas las pruebas se ejecutaron correctamente!")
    else:
        print("\nAlgunas pruebas fallaron. Revisa el reporte para mas detalles.")
        sys.exit(1)