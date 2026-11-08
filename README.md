# Bosques Aleatorios (*Random Forest*)

Presentación interactiva y educativa sobre el algoritmo **Random Forest**, sus fundamentos matemáticos (Teorema de Condorcet), la doble aleatoriedad de Leo Breiman, auditoría con Explainable AI (SHAP), limitaciones de extrapolación y arquitectura de despliegue en producción con ONNX Runtime.

**Autor:** Denshel David Mérida Quispe  
**Inspiración de diseño:** [MLU-Explain](https://mlu-explain.github.io/) y [Distill.pub](https://distill.pub/)

## Estructura de la Presentación (15 Diapositivas)

1. **Portada:** Presentación minimalista y limpia.
2. **Teorema del Jurado de Condorcet (1785):** Fundamento de la agregación democrática y simulador binomial interactivo.
3. **Caso de Estudio: Señales Viales:** Clasificación en espacio de 4 características ($p = 4$) y comparación con árbol rígido.
4. **Doble Aleatoriedad (1. Bagging):** Muestreo con reemplazo y deducción del Out-of-Bag (OOB $\approx 36.8\%$).
5. **Doble Aleatoriedad (2. Subespacio Aleatorio):** Ocultación aleatoria de variables en nodos ($m \approx \sqrt{p}$).
6. **Descorrelación y Reducción de Varianza:** Fórmula de balance $\text{Var}(\text{Ensemble}) \approx \rho \sigma^2 + \frac{1 - \rho}{B} \sigma^2$.
7. **Matriz de Predicciones:** Cuadrícula interactiva de 9 árboles $\times$ 6 señales con cancelación de error residual.
8. **Auditoría con XAI (SHAP vs Gini):** Limitaciones de Gini MDI frente a los valores de Shapley direccionales.
9. **Laboratorio SHAP:** Gráfico de dispersión *Beeswarm Plot* interactivo con filtros dinámicos.
10. **Límite Matemático: Fallo de Extrapolación:** Partición en hiperrectángulos ortogonales y cota $\max(Y_{\text{train}})$.
11. **Demostración en Vivo:** Gráfico dinámico en Chart.js comparando regresión lineal vs. aplanamiento de Random Forest.
12. **Arquitectura: Notebook a Producción:** Desacoplamiento con ONNX Runtime en contenedores distroless.
13. **Hardware y Paralelismo:** Algoritmo *embarrassingly parallel* en hilos de CPU sin locks de memoria.
14. **Matriz de Decisión Técnica:** Criterios de cuándo SÍ seleccionarlo vs. cuándo DESCARTARLO.
15. **Asistente de Decisión (Quiz):** Diagnóstico interactivo en 3 preguntas para selección de algoritmos.

## Ejecución

No requiere empaquetadores ni dependencias locales. Basta con abrir `index.html` en cualquier navegador web moderno:

- **Navegación:** Teclas `←` / `→` o `Espacio`.
- **Pantalla completa:** Tecla `F`.
- **Atajos:** Tecla `?`.
