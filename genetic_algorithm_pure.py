import random

# ==========================================
# 1. REPRESENTASI INDIVIDU & ATURAN MAIN
# ==========================================
TARGET_KATA = "GENETIKA"
TARGET = [7, 5, 14, 5, 20, 9, 11, 1]
JUMLAH_GEN = len(TARGET)
NILAI_MAKS_ALLELE = 26
JUMLAH_POPULASI = 10
PROB_CROSSOVER = 0.8
PROB_MUTASI = 0.1

def konversi_ke_huruf(individu):
    return "".join([chr(gen + 64) for gen in individu])

# ==========================================
# 2. PEMBANGKITAN POPULASI AWAL
# ==========================================
def bangkitkan_populasi(jumlah):
    return [[random.randint(1, NILAI_MAKS_ALLELE) for _ in range(JUMLAH_GEN)] for _ in range(jumlah)]

# ==========================================
# 3. EVALUASI FITNESS
# ==========================================
def hitung_fitness(individu):
    total_selisih = sum(abs(i - t) for i, t in zip(individu, TARGET))
    return (JUMLAH_GEN * NILAI_MAKS_ALLELE) - total_selisih

# ==========================================
# 4. SELEKSI (MESIN ROULLETE)
# ==========================================
def seleksi_roullete(populasi, fitness_populasi):
    total_fitness = sum(fitness_populasi)
    probabilitas = [f / total_fitness for f in fitness_populasi]
    
    induk_terpilih = []
    for _ in range(JUMLAH_POPULASI):
        r = random.random()
        komulatif = 0
        for i, prob in enumerate(probabilitas):
            komulatif += prob
            if r <= komulatif:
                induk_terpilih.append(populasi[i])
                break
    return induk_terpilih

# ==========================================
# 5. REPRODUKSI (CROSSOVER & MUTASI)
# ==========================================
def crossover(induk1, induk2):
    anak1, anak2 = induk1[:], induk2[:]
    if random.random() < PROB_CROSSOVER:
        for i in range(JUMLAH_GEN):
            if random.random() < 0.5:
                anak1[i], anak2[i] = anak2[i], anak1[i]
    return anak1, anak2

def mutasi(individu):
    anak = individu[:]
    for i in range(JUMLAH_GEN):
        if random.random() < PROB_MUTASI:
            geser = random.randint(-5, 5)
            anak[i] += geser
            anak[i] = max(1, min(NILAI_MAKS_ALLELE, anak[i])) 
    return anak

# ==========================================
# PROGRAM UTAMA
# ==========================================
def genetic_algorithm():
    populasi = bangkitkan_populasi(JUMLAH_POPULASI)
    generasi = 0
    ditemukan = False
    
    while not ditemukan:
        generasi += 1
        fitness_populasi = [hitung_fitness(ind) for ind in populasi]
        
        max_fit = max(fitness_populasi)
        best_ind = populasi[fitness_populasi.index(max_fit)]
        
        # Format :02d ditambahkan di sini agar tampil sebagai 01, 02, dst.
        print(f"Generasi {generasi:02d} | Terbaik: {konversi_ke_huruf(best_ind)} {best_ind} | Fitness: {max_fit}")
        
        if max_fit == (JUMLAH_GEN * NILAI_MAKS_ALLELE):
            print(f"\n=> BERHASIL! Target Ditemukan pada Generasi {generasi:02d}: {konversi_ke_huruf(best_ind)} {best_ind}")
            ditemukan = True
            break
            
        induk = seleksi_roullete(populasi, fitness_populasi)
        
        anak_baru = []
        for i in range(0, JUMLAH_POPULASI, 2):
            induk1 = induk[i]
            induk2 = induk[(i+1) % JUMLAH_POPULASI]
            anak1, anak2 = crossover(induk1, induk2)
            anak_baru.extend([mutasi(anak1), mutasi(anak2)])
            
        # 6. ELITISM
        populasi_gabungan = populasi + anak_baru
        fitness_gabungan = [hitung_fitness(ind) for ind in populasi_gabungan]
        populasi_terurut = [x for _, x in sorted(zip(fitness_gabungan, populasi_gabungan), reverse=True)]
        populasi = populasi_terurut[:JUMLAH_POPULASI]

if __name__ == "__main__":
    genetic_algorithm()
