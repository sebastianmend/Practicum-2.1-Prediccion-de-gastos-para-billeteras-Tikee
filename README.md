<div align="center">
  
<img src="https://cdn.discordapp.com/attachments/1065809341103493135/1294019463703826513/Logo_tikee_sin_fondo.png?ex=670e1a49&is=670cc8c9&hm=ab7a45b0155cb44163af2a076fdb3ce32bacd5f04ab800217019cdb05bf968c9&" alt="Temas a practicar" width="100"/>

# Reto: Predicción de Gastos para Billeteras de Aplicaciones Financieras 💻

Equipo de trabajo: [Sebastian Mendieta](https://github.com/sebastianmend) y [Jean Villavicencio](https://github.com/Jeanvillav)

</div>

## Resumen
El reto busca desarrollar un servicio de predicción de gastos para billeteras digitales en aplicaciones financieras, que prediga automáticamente pagos recurrentes basados en los patrones de consumo y geolocalización de los usuarios. La solución tiene como objetivo mejorar la eficiencia y conveniencia de los pagos automáticos, generando notificaciones inteligentes que sugieran realizar transacciones en momentos y lugares relevantes para el usuario, reduciendo la carga manual.

## Propuestas de Modelos

### 1. ARIMA/SARIMA (AutoRegressive Integrated Moving Average con componentes estacionales)
**Ventajas**:
- **Bien establecido**: Es uno de los métodos más usados en la predicción de series temporales.
- **Fácil de interpretar**: Los componentes (autoregresión, diferencia y media móvil) son claros y ajustables.
- **Manejo de estacionalidad**: SARIMA captura patrones estacionales como pagos mensuales.
- **Rendimiento en datos lineales**: Funciona bien cuando las relaciones en los datos son lineales.

**Desventajas**:
- **Limitado en relaciones no lineales**: No maneja bien patrones complejos no lineales.
- **Difícil manejo de múltiples variables**: Incorpora otras características (como geolocalización o comportamiento) con dificultad.
- **Ajuste manual**: Requiere ajustar parámetros como p, d, q y estacionalidad, lo que puede ser tedioso.

### 2. Prophet (desarrollado por Facebook)
**Ventajas**:
- **Sencillo de usar**: Fácil implementación con mínimo ajuste de parámetros.
- **Manejo de estacionalidad compleja**: Captura estacionalidades diarias, semanales y anuales.
- **Robusto ante valores atípicos**: Tolerante a datos faltantes y anomalías.
- **Predicciones explicables**: Los componentes son interpretables (tendencias, estacionalidad, etc.).
- **Escalabilidad**: Funciona bien con grandes volúmenes de datos y es fácil de implementar en producción.

**Desventajas**:
- **Interacciones limitadas**: No está optimizado para manejar múltiples características complejas como geolocalización o comportamiento.
- **Limitado en patrones no lineales**: Aunque mejor que ARIMA, sigue teniendo limitaciones frente a relaciones no lineales complejas.

### 3. LSTM (Long Short-Term Memory)
**Ventajas**:
- **Captura dependencias a largo plazo**: Ideal para relaciones temporales a largo plazo en patrones de gasto recurrentes.
- **Manejo de no linealidad**: Funciona bien con relaciones no lineales frecuentes en los hábitos de consumo.
- **Flexibilidad para múltiples características**: Integra múltiples fuentes de datos (geolocalización, tipo de gasto, etc.).
- **Aprendizaje secuencial**: Excelente para datos secuenciales donde el orden de los eventos es relevante.

**Desventajas**:
- **Mayor complejidad**: Requiere más tiempo para ajustar y entrenar en comparación con Prophet o ARIMA.
- **Demanda de datos**: Necesita grandes volúmenes de datos para funcionar bien.
- **Difícil de interpretar**: Las predicciones son más difíciles de interpretar, ya que actúa como una "caja negra".

## Conclusión: Mejor Modelo para el Reto
Dado el contexto de predicción de pagos recurrentes para billeteras financieras, **LSTM** es probablemente la mejor opción. Las razones principales son:

- **Dependencias a largo plazo**: Captura relaciones temporales complejas entre patrones de consumo, geolocalización y otros factores.
- **Flexibilidad**: Permite combinar datos temporales con otras variables dinámicas, mejorando la precisión en escenarios complejos.

**Prophet** podría ser una opción razonable si los datos siguen patrones simples y se busca un modelo rápido de implementar y más interpretable. Sin embargo, **LSTM** es más adecuado para este tipo de problema con múltiples fuentes de datos y relaciones no lineales.

## Comparación en Mantenimiento y Retroalimentación

### LSTM
- **Alto mantenimiento**: Requiere retroalimentación continua, actualizaciones regulares y reentrenamiento frecuente.
- **Alto grado de intervención**: Es necesario un monitoreo constante para asegurar que las predicciones sean precisas.

### Prophet
- **Bajo mantenimiento**: Necesita menos reentrenamiento y ajustes, ya que maneja tendencias y estacionalidades de manera autónoma.
- **Menor intervención manual**: Es más resistente a variaciones en los datos, lo que reduce la necesidad de monitoreo constante.

## Resumen
Si se dispone de los recursos para realizar ajustes y retroalimentaciones continuas, **LSTM** es más potente para capturar patrones complejos. Si se busca algo más sencillo de mantener, **Prophet** es más adecuado.

