<div align="center">
  
<img src="https://i.imgur.com/WB9OFRy.png" alt="Logo tikee" width="100"/>

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

- Si los pagos recurrentes siguen un patrón bastante regular (con poca fluctuación o cambios importantes en los hábitos de consumo de los usuarios), ARIMA o Prophet serían las opciones más recomendadas:
ARIMA es mejor si tus datos son estacionarios y el comportamiento es lineal.
Prophet sería útil si hay estacionalidad clara y eventos especiales que afectan a los pagos (por ejemplo, más pagos a fin de mes o durante feriados).
- Si los patrones de consumo y pagos cambian con el tiempo y dependen de múltiples factores (como geolocalización, día de la semana, etc.), entonces LSTM es la opción más robusta:
LSTM es ideal cuando los datos son no lineales y los pagos dependen de muchos factores que cambian a lo largo del tiempo.

Si se dispone de los recursos para realizar ajustes y retroalimentaciones continuas, **LSTM** es más potente para capturar patrones complejos. Si se busca algo más sencillo de mantener, **Prophet** es más adecuado.


## Preguntas para la reunión con la empresa:

Sobre los requisitos del proyecto:

- **Clarificación del objetivo principal:** ¿Qué objetivos clave tiene la empresa con la predicción de gastos en billeteras digitales? ¿Buscan reducir costos, mejorar la experiencia del usuario o incrementar las transacciones?
 
- **Patrones de consumo:** ¿Existen patrones de consumo previamente usados? ¿Tienen ejemplos de patrones específicos que esperan que detectemos?

- **Uso de geolocalización:** ¿Cómo esperan que la geolocalización influya en las predicciones? ¿Tienen casos de uso sobre cómo la ubicación debería afectar los pagos recurrentes o sugeridos?

- **Disponibilidad de datos:** 

¿Qué tipos de datos de usuario estarán disponibles (transacciones, ubicaciones, hábitos de uso)? 

*Nos ineresa mucho*

- **Interacción con otros sistemas:** ¿La billetera digital está integrada con otros sistemas o plataformas (como bancos o servicios externos) que debamos tener en cuenta? Si es así, ¿cómo será la integración?

- **Notificaciones:** ¿Tienen una expectativa de cuántas notificaciones deberían enviarse para que el usuario no se sienta abrumado? ¿Prefieren notificaciones basadas en tiempo o en eventos específicos?

- **Limitaciones actuales:** ¿Cuáles son las principales limitaciones o desafíos que enfrentan actualmente en cuanto a la predicción de pagos? ¿Qué esperan que resolvamos con la solución propuesta?

- **Criterios de éxito:** ¿Cómo medirán el éxito del proyecto? ¿Cuáles son los KPIs más relevantes (por ejemplo, aumento en pagos automáticos, reducción de fricción en el uso de la aplicación)?

- **Recursos disponibles:** ¿Qué herramientas, bibliotecas o tecnologías ya utilizan o recomiendan que usemos para el desarrollo del proyecto (por ejemplo, algún sistema de mensajería en tiempo real, APIs de geolocalización)?

- **Herramientas y plataformas preferidas:** ¿La empresa tiene alguna preferencia en cuanto a las tecnologías que deberíamos usar para el desarrollo del prototipo? (por ejemplo, lenguajes, frameworks, sistemas de bases de datos, etc.)

