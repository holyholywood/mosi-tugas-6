import math

print("NIM \t: 10118181")
print("Nama \t: Ditotisi Rasyid Sumpena")
print("Kelas \t: IF-5")

# Mencari Waktu Antar  Kedatangan  Konsumen
a = 19
a2 = 3
m = 43
m2 = 43
zseed = 10118181
zseed2 = 10118181
p = 30
q = 48
sb = 20
rt = 50
i = 1
wsdd2 = 0
ratatemp = 0
print("Asumsi \t: a = ", a, " ", a2, " m = ", m, " ", m2, " Z0 = ", zseed)
print(
    "+----+------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+"
)
print(
    "|    |                Bilangan Acak yang Dibangkitkan             |                                                                                                   SIMULASI                                                                                                                      |"
)
print(
    "+----+----------------------------------+-------------------------+------------------------------------------+----------------------------------------+---------------------------------+--------------------------------+----------------------------------+---------------------------------------+"
)
print(
    "| No | waktu Antar Kedatangan Kendaraan | Waktu Proses Pembayaran | Waktu Antar Kedatangan Kendaraan (detik) | Kumulatif Kedatangan Kendaraan (detik) | Waktu Proses Pembayaran (detik) | Waktu Selesai Dilayani (detik) | Waktu Menunggu Kendaraan (detik) | Waktu Menganggur Mesin sensor (detik) |"
)
print(
    "+----+----------------------------------+-------------------------+------------------------------------------+----------------------------------------+---------------------------------+--------------------------------+----------------------------------+---------------------------------------+"
)
while i <= 20:

    # kedatangan UI
    zi = (a * zseed) % m
    ui = zi / m
    zseed = zi

    # Pembayaran UI
    zi2 = (a2 * zseed2) % m2
    ui2 = zi2 / m2
    zseed2 = zi2

    # Waktu Antar Kedatangan kendaraan
    wakk = p + ((q - p) * ui)

    # kumulatif kedatangan
    if i == 1:
        kk = wakk
    else:
        kk = kk + wakk

    # waktu proses pembayaran detik
    # ui2 urgent
    zi2ur = (a2 * zseed2) % m2
    ui2ur = zi2ur / m2
    ln = math.log(ui2)
    pangkat = math.pow((-2 * ln), (1 / 2))
    xin = math.sin((2 * 3.14) * ui2ur)
    wppd = rt + (sb * (pangkat * xin))

    # waktu selesai dilayani detik
    wsddtemp = wsdd2
    wsdd = kk + wppd
    wsdd2 = wsdd

    # waktu menunggu kendaraan detik

    if i == 1:
        wmkd = 0
    else:
        wmkd = wsddtemp - kk
        if wmkd < 0:
            wmkd = 0
        else:
            wmkd = wmkd

    # wmmsd
    if i == 1:
        wmmsd = kk
    else:
        if wmkd == 0:
            wmmsd = wsddtemp - kk
        else:
            wmmsd = 0
    ratatemp = ratatemp + wmkd
    # output
    if i <= 9:
        if wmkd >= 9:
            print(
                "|",
                i,
                " |\t\t",
                "{0:.3f}".format(ui),
                "\t\t\t|\t",
                "{0:.3f}".format(ui2),
                "\t\t  |\t\t\t",
                "{0:.0f}".format(wakk),
                "\t\t     |\t\t\t",
                "{0:.0f}".format(kk),
                "\t\t      |\t\t",
                "{0:.0f}".format(wppd),
                "\t\t\t|\t\t",
                "{0:.0f}".format(wsdd),
                "\t\t |\t\t",
                "{0:.0f}".format(wmkd),
                "\t\t    |\t\t\t",
                "{0:.0f}".format(wmmsd),
                "\t\t    |",
            )
        else:
            print(
                "|",
                i,
                " |\t\t",
                "{0:.3f}".format(ui),
                "\t\t\t|\t",
                "{0:.3f}".format(ui2),
                "\t\t  |\t\t\t",
                "{0:.0f}".format(wakk),
                "\t\t     |\t\t\t",
                "{0:.0f}".format(kk),
                "\t\t      |\t\t",
                "{0:.0f}".format(wppd),
                "\t\t\t|\t\t",
                "{0:.0f}".format(wsdd),
                "\t\t |\t\t",
                "{0:.0f}".format(wmkd),
                "\t\t    |\t\t\t",
                "{0:.1f}".format(abs(wmmsd)),
                "\t\t    |",
            )

    else:
        if wmkd > 9:
            print(
                "|",
                i,
                "|\t\t",
                "{0:.3f}".format(ui),
                "\t\t\t|\t",
                "{0:.3f}".format(ui2),
                "\t\t  |\t\t\t",
                "{0:.0f}".format(wakk),
                "\t\t     |\t\t\t",
                "{0:.0f}".format(kk),
                "\t\t      |\t\t",
                "{0:.0f}".format(wppd),
                "\t\t\t|\t\t",
                "{0:.0f}".format(wsdd),
                "\t\t |\t\t",
                "{0:.0f}".format(wmkd),
                "\t\t    |\t\t\t",
                "{0:.0f}".format(wmmsd),
                "\t\t    |",
            )
        else:
            print(
                "|",
                i,
                "|\t\t",
                "{0:.3f}".format(ui),
                "\t\t\t|\t",
                "{0:.3f}".format(ui2),
                "\t\t  |\t\t\t",
                "{0:.0f}".format(wakk),
                "\t\t     |\t\t\t",
                "{0:.0f}".format(kk),
                "\t\t      |\t\t",
                "{0:.0f}".format(wppd),
                "\t\t\t|\t\t",
                "{0:.0f}".format(wsdd),
                "\t\t |\t\t",
                "{0:.0f}".format(wmkd),
                "\t\t    |\t\t\t",
                "{0:.1f}".format(abs(wmmsd)),
                "\t\t    |",
            )

    i = i + 1
print(
    "+----+----------------------------------+-------------------------+------------------------------------------+----------------------------------------+---------------------------------+--------------------------------+----------------------------------+---------------------------------------+"
)
ratarata = ratatemp / 20
print(
    "Hasil Rata-Rata waktu  menunggu sebuah kendaraan untuk dapat melakukan pembayaran : ",
    ratarata,
)

print(
    "\nUntuk Kerapihan dan besar kolom saya menggunakan width : 500 pada Screen Buffer Size dan unchecklist Wrap Text Output on resize pada properties terminal"
)
