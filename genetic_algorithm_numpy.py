import numpy as np

TARGET = np.array([7, 5, 14, 5, 20, 9, 11, 1])
JUMLAH_GEN = len(TARGET)
MAKS_ALLELE = 26
JUMLAH_POPULASI = 10
PROB_CROSS = 0.8
PROB_MUT = 0.1

def konversi_ke_huruf(individu):
    return "".join([chr(gen + 64) for gen in individu])

def genetic_algorithm_numpy():
    populasi = np.random.randint(1, MAKS_ALLELE + 1, size=(JUMLAH_POPULASI, JUMLAH_GEN))
    generasi = 0
    
    while True:
        generasi += 1
        
        selisih = np.sum(np.abs(populasi - TARGET), axis=1)
        fitness = (JUMLAH_GEN * MAKS_ALLELE) - selisih
        
        best_idx = np.argmax(fitness)
        
        # Format :02d ditambahkan di sini
        print(f"Generasi {generasi:02d} | Terbaik: {konversi_ke_huruf(populasi[best_idx])} {populasi[best_idx].tolist()} | Fitness: {fitness[best_idx]}")
        
        if fitness[best_idx] == JUMLAH_GEN * MAKS_ALLELE:
            print(f"\n=> BERHASIL! Target ditemukan di generasi {generasi:02d}: {konversi_ke_huruf(populasi[best_idx])} {populasi[best_idx].tolist()}")
            break
            
        probabilitas = fitness / fitness.sum()
        indeks_terpilih = np.random.choice(np.arange(JUMLAH_POPULASI), size=JUMLAH_POPULASI, p=probabilitas)
        induk = populasi[indeks_terpilih]
        
        anak = np.copy(induk)
        for i in range(0, JUMLAH_POPULASI, 2):
            if np.random.rand() < PROB_CROSS:
                mask = np.random.rand(JUMLAH_GEN) < 0.5
                anak[i][mask], anak[i+1][mask] = anak[i+1][mask], anak[i][mask]
                
        mask_mutasi = np.random.rand(JUMLAH_POPULASI, JUMLAH_GEN) < PROB_MUT
        geser = np.random.randint(-5, 6, size=(JUMLAH_POPULASI, JUMLAH_GEN))
        anak[mask_mutasi] += geser[mask_mutasi]
        anak = np.clip(anak, 1, MAKS_ALLELE)
        
        populasi_gabungan = np.vstack((populasi, anak))
        fitness_gabungan = (JUMLAH_GEN * MAKS_ALLELE) - np.sum(np.abs(populasi_gabungan - TARGET), axis=1)
        indeks_terbaik = np.argsort(fitness_gabungan)[::-1][:JUMLAH_POPULASI]
        populasi = populasi_gabungan[indeks_terbaik]

if __name__ == "__main__":
    genetic_algorithm_numpy()
