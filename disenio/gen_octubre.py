#!/usr/bin/env python3
"""Segunda tanda de @hcarg.app: 15 publicaciones del 18/09 al 16/10.

Continua el reparto por pilar de la primera tanda (dolor 30%, producto 30%,
confianza 25%, prueba 15%) pero sin repetir angulos: los temas nuevos entran
por el costado del ejercicio profesional, no por el software.

Sin precios. En temas legales se aclara que el software ayuda pero el
responsable es el profesional.
"""
from marca_hc import *


# ==========================================================================
def p16_lo_que_no_se_ve():
    return texto_suelto(
        "EL TRABAJO INVISIBLE",
        "Nadie te paga por administrar tu consultorio.",
        "Y sin embargo son horas todos los meses: registros, turnos, cobros, "
        "facturas. Trabajo real que no aparece en ninguna factura, ni en el "
        "cálculo de cuánto vale tu hora.",
        "PERO SÍ APARECE EN TU CANSANCIO", "blanco")


def p17_derecho_de_acceso():
    return [
        ("hc17_acceso_1.png", portada(
            "Un paciente te pide", "su historia clínica",
            "Qué tenés que hacer, y en cuánto tiempo.", "teal")),
        ("hc17_acceso_2.png", punto(
            None, "Tiene derecho a pedirla.",
            "La historia clínica le pertenece al paciente. Vos sos el custodio: "
            "podés negarte a muchas cosas, pero no a entregarle una copia.", 1)),
        ("hc17_acceso_3.png", punto(
            None, "El plazo es corto.",
            "La ley habla de entrega dentro de las 48 horas para lo urgente. "
            "Si tus registros están en un cuaderno o repartidos en carpetas, "
            "ese plazo se vuelve un problema.", 2)),
        ("hc17_acceso_4.png", punto(
            None, "Tiene que ser legible y completa.",
            "No alcanza con juntar papeles sueltos: se entrega el registro "
            "ordenado y cronológico de las actuaciones.", 3)),
        ("hc17_acceso_5.png", punto(
            None, "Y queda constancia de la entrega.",
            "Conviene registrar que la pediste, quién la retiró y cuándo. "
            "Esa constancia te protege a vos.", 4)),
        ("hc17_acceso_6.png", cta(
            "En HC ARG son dos clics",
            "Exportás la historia completa en PDF, ordenada y con la firma del "
            "profesional. Lo que hoy te lleva una tarde.",
            "PROBALO GRATIS · LINK EN BIO", None, "teal")),
    ]


def p18_ficha_pdf():
    return placa_captura(
        "EXPORTAR",
        "La historia clínica completa, en un PDF.",
        "Ordenada, cronológica y con tus datos profesionales. Lista para "
        "entregarle al paciente o para presentar donde te la pidan.",
        "HC.png", (0.005, 0.04, 0.40, 0.52))


def p19_precio_de_la_hora():
    return texto_suelto(
        "UNA CUENTA INCÓMODA",
        "Dividí lo que facturaste por las horas que le dedicaste.",
        "No solo las de sesión: sumá las de administración, las de buscar un "
        "dato, las de facturar. El número que sale casi nunca coincide con lo "
        "que creés que cobrás por hora.",
        None, "rosa")


def p20_privacidad_practica():
    return [
        ("hc20_privacidad_1.png", portada(
            "Confidencialidad", "en la práctica",
            "Cinco cosas concretas, más allá del juramento.", "blanco")),
        ("hc20_privacidad_2.png", punto(
            None, "El riesgo no es un hacker.",
            "Es tu notebook en un café, el celular que se pierde, alguien que "
            "abre tu computadora en casa. Lo cotidiano.", 1)),
        ("hc20_privacidad_3.png", punto(
            None, "Un archivo sin cifrar es texto plano.",
            "Cualquiera que tenga el equipo lo abre. La contraseña de Windows "
            "no protege el disco: solo la sesión.", 2)),
        ("hc20_privacidad_4.png", punto(
            None, "El grupo de WhatsApp no es un lugar.",
            "Comentar un caso por mensajería, aunque sea sin nombre, deja un "
            "registro en servidores que no controlás.", 3)),
        ("hc20_privacidad_5.png", punto(
            None, "Los adjuntos también son historia clínica.",
            "El informe que te mandaron, la foto del estudio, el mail. Todo eso "
            "es dato sensible y merece el mismo cuidado.", 4)),
        ("hc20_privacidad_6.png", punto(
            None, "Y alguien debería poder auditar.",
            "Saber quién accedió a qué y cuándo no es burocracia: es lo que te "
            "permite demostrar que hiciste las cosas bien.", 5)),
        ("hc20_privacidad_7.png", cta(
            "Todo esto está resuelto",
            "Cifrado local, adjuntos dentro de la misma base, auditoría de "
            "accesos y copias verificadas. No hay que acordarse de nada.",
            "PROBALO GRATIS · LINK EN BIO", "HCARG.COM.AR", "blanco")),
    ]


def p21_agenda():
    return placa_captura(
        "AGENDA",
        "Los turnos, sincronizados con tu calendario.",
        "Se integra con Google Calendar y ya trae los feriados argentinos. "
        "Reprogramás en la app y se actualiza donde lo mires.",
        "REPORTES.png", (0.00, 0.17, 0.55, 0.70))


def p22_empezar_de_cero():
    return texto_suelto(
        "LA OBJECIÓN MÁS COMÚN",
        "«Tengo diez años de historias en papel.»",
        "No hace falta cargar nada retroactivo. Empezás con los pacientes que "
        "atendés esta semana y el papel queda como archivo. En dos meses la "
        "mayor parte de tu práctica ya está adentro.",
        "NO ES TODO O NADA", "teal")


def p23_dia_tipico():
    return [
        ("hc23_dia_1.png", portada(
            "Un día con HC ARG", "de principio a fin",
            "Cómo cambia la semana, en concreto.", "rosa")),
        ("hc23_dia_2.png", punto(
            "8:55", "Abrís la app antes del primer paciente.",
            "Ves los turnos del día y, en cada uno, la última sesión. Llegás "
            "sabiendo dónde quedaste.")),
        ("hc23_dia_3.png", punto(
            "DURANTE", "Escribís la sesión al terminar.",
            "Dos minutos, con el paciente todavía fresco. No a la noche, "
            "cuando ya se mezclaron cinco.")),
        ("hc23_dia_4.png", punto(
            "AL CERRAR", "Marcás lo cobrado.",
            "Un clic por sesión. Eso alimenta solo el reporte de ingresos y "
            "la facturación del mes.")),
        ("hc23_dia_5.png", punto(
            "FIN DE MES", "Facturás todo junto.",
            "La app arma las Factura C, se conecta con ARCA y trae el CAE. "
            "Lo que antes era un domingo entero.")),
        ("hc23_dia_6.png", cta(
            "No es más trabajo",
            "Es el mismo trabajo, repartido en momentos donde ya estás ahí. "
            "Probalo con dos pacientes y fijate.",
            "PROBALO GRATIS · LINK EN BIO", "HCARG.COM.AR", "rosa")),
    ]


def p24_soporte():
    return texto_suelto(
        "DEL OTRO LADO",
        "Si algo no funciona, me escribís a mí.",
        "No hay mesa de ayuda ni ticket que se pierde. Soy psicólogo y "
        "desarrollé esto para mi propio consultorio, así que entiendo el "
        "problema antes de que termines de explicarlo.",
        None, "blanco")


def p25_cierre_octubre():
    return cta(
        "Dos pacientes, sin tarjeta",
        "La versión de prueba no vence y tiene todas las funciones. "
        "Cargá dos pacientes reales y usala un mes entero.",
        "DESCARGALO · LINK EN BIO", "HCARG.COM.AR", "teal")


def main():
    placas = []
    placas.append(("hc16_trabajo_invisible.png", p16_lo_que_no_se_ve()))
    placas += p17_derecho_de_acceso()
    placas.append(("hc18_exportar.png", p18_ficha_pdf()))
    placas.append(("hc19_precio_hora.png", p19_precio_de_la_hora()))
    placas += p20_privacidad_practica()
    placas.append(("hc21_agenda.png", p21_agenda()))
    placas.append(("hc22_empezar.png", p22_empezar_de_cero()))
    placas += p23_dia_tipico()
    placas.append(("hc24_soporte.png", p24_soporte()))
    placas.append(("hc25_cierre.png", p25_cierre_octubre()))
    guardar(placas, "preview_octubre_hc.jpg", cols=7)


if __name__ == "__main__":
    main()
