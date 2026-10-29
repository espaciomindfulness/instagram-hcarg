# Cuenta en pausa — 28/10/2026

@hcarg.app queda en pausa por decisión de Christian.

## Por qué

Dos meses y medio publicando día por medio, 25 publicaciones, y la cuenta
pasó de 37 a 37 seguidores. Cero crecimiento, medido semana a semana desde el
4 de septiembre. En el mismo período Espacio Mindfulness sumó 318 y la cuenta
personal se mantuvo. El tiempo de producción rinde más en las otras dos.

No es que el contenido fuera malo: el alcance promedio era del 44% de la base,
muy por encima del 4% de EM. El problema es la base — 37 personas — y que
publicar más no la hacía crecer.

## Qué quedó andando y qué no

| Workflow | Estado | Por qué |
|---|---|---|
| Publicar en Instagram | **cron apagado** | No hay contenido nuevo que publicar |
| Refrescar token | **sigue activo** | Crítico: si el token vence hay que rehacer el alta en Meta |
| Medir seguidores | sigue activo | Cuesta nada y avisa si algo se mueve solo |
| Rendimiento | sigue activo | Idem |

Los dos últimos posteos ya hechos (30/10 y 01/11) siguen en el calendario. Si
se los quiere publicar, se dispara **Actions → Publicar en Instagram → Run
workflow** el día que corresponda.

## Cómo reactivarla

1. Descomentar el `schedule` en `.github/workflows/publicar.yml`.
2. Cargar contenido nuevo en `contenido/calendario.json`.
3. `python scripts/validar.py` y pushear.

No hace falta tocar nada en Meta ni en los Secrets **siempre que el refresco
de token siga corriendo**. Si llegara a fallar varias semanas seguidas, el
token vence a los 60 días y ahí sí hay que rehacer el alta.

## Si alguna vez se retoma, qué probar

El único reel que se publicó llegó a **131 cuentas**; los carruseles
promediaron 14 y las imágenes 6. Diez veces más. Si se vuelve, conviene
volver con grabaciones de pantalla de la app en vez de placas.
