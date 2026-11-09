# Bosques Aleatorios (*Random Forest*): Presentación Teórica y Didáctica

Presentación teórica, estructurada y educativa sobre el algoritmo **Random Forest** (*Bosques Aleatorios*), su justificación ante la inestabilidad de los árboles de decisión individuales, sus tres pilares matemáticos, un ejemplo práctico directo y sus criterios técnicos críticos en la industria.

**Autor:** Denshel David Mérida Quispe  
**Enfoque:** Exposición Académica Oral (Teoría Primero + Ejemplos Cortos e Ilustrativos)

---

## 📚 Estructura de la Exposición (12 Diapositivas)

1. **Portada & Mapa de Ruta:** Introducción general, datos del autor y los 6 módulos temáticos.
2. **1. ¿Qué es Random Forest? (Contexto General):** Definición de aprendizaje en ensamble (*ensemble learning*) y la analogía médica del comité de expertos frente al especialista solitario.
3. **2. El Problema que Resuelve: Inestabilidad del Árbol Individual:** ¿Cómo piensa un árbol?, alta varianza, sobreajuste (*overfitting*) y cómo promediar muchos árboles elimina la inestabilidad.
4. **3. Pilar A: La Sabiduría de las Masas (Teorema de Condorcet, 1785):** Premisa de mayoría democrática, escala demostrativa de precisión (60% $\to$ 65% $\to$ 75%) y la condición de oro de independencia.
5. **3. Pilar B: Bagging (Muestreo con Reemplazo):** Creación de mundos paralelos de datos y el conjunto *Out-of-Bag* ($\approx 37\%$) para validación automática.
6. **3. Pilar C: Subespacio de Características:** Ruptura del monopolio de variables dominantes ocultando variables en cada bifurcación para forzar diversidad.
7. **4. El Ejemplo Práctico: Señales de Cruce Peatonal:** 4 variables (tamaño, forma, colores, contenido), fallo del árbol rígido ("redonda jamás es cruce") y éxito del bosque por voto 2 a 1.
8. **5. Criterio Técnico A: Interpretabilidad Real con SHAP:** Limitaciones de la métrica clásica Gini (sin signo) y valores de Shapley con dirección (+ / -) para auditoría ética.
9. **5. Criterio Técnico B: El Límite Matemático de Extrapolación:** Por qué los árboles dividen en cajas ortogonales, no pueden predecir récords históricos ($f(x) \le \max(Y_{\text{train}})$) y se aplanan en series de tiempo con tendencia.
10. **5. Criterio Técnico C: Hardware y Despliegue con ONNX:** Paralelismo masivo en núcleos de CPU y exportación a binarios ONNX para inferencia rápida en C# (.NET) o Go sin Python.
11. **6. Resumen de Decisión Técnica: Cuándo SÍ vs. Cuándo NO:** Matriz de decisión definitiva en dos columnas de alto contraste.
12. **Conclusiones & Ronda de Preguntas:** Síntesis de los 4 aprendizajes clave y apertura de preguntas con el tribunal.

---

## 🎯 Elementos Didácticos en Cada Diapositiva

- **🎯 Objetivo de la Diapositiva:** Qué meta conceptual domina la audiencia al finalizar la lámina.
- **📖 Teoría Fundamental:** Desarrollo teórico claro, limpio y legible, ideal para leer en proyector.
- **🔍 Ilustración / Ejemplo Corto y Directo:** Demostración gráfica inmediata en 5 segundos sin interactividad engorrosa ni distracciones.
- **💡 Conclusión Clave (*Takeaway*):** Regla de oro para recordar.
- **🎙️ Guión del Expositor (Tecla `N`):** Panel lateral con el discurso oral sugerido palabra por palabra y consejos didácticos.

---

## 🚀 Controles de Navegación

Abre directamente `index.html` en cualquier navegador:

- **Avanzar / Retroceder:** Teclas `←` / `→` o barra de `Espacio`.
- **🎙️ Guión Oral del Expositor:** Tecla `N` (abre/cierra el panel con el libreto para hablar).
- **Pantalla Completa:** Tecla `F`.
- **Atajos de Ayuda:** Tecla `?`.
- **Cerrar Paneles:** Tecla `Esc`.
