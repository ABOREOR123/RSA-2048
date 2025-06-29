# 📜 Reporte: Explicación Matemática de AES-128 + RSA-2048  
**Autor**: DeepSeek Chat  
**Fecha**: 11 de junio de 2025  

---

## 🔐 **Introducción**  
La combinación de **AES-128** (cifrado simétrico) y **RSA-2048** (cifrado asimétrico) es fundamental en seguridad informática moderna. Este documento detalla su funcionamiento matemático y su integración en sistemas híbridos.  

---

## 1. **AES-128: Cifrado Simétrico**  
### 1.1 Conceptos Clave  
- **Tamaño de bloque**: 128 bits (16 bytes).  
- **Clave**: 128 bits (10 rondas).  
- **Operaciones en GF(2⁸)**: Cada byte se trata como un polinomio en el campo finito \( \mathbb{F}_{2^8} \).  

### 1.2 Estructura Matemática  
1. **SubBytes**:  
   - Sustitución no lineal usando la S-box (inversión multiplicativa en \( \mathbb{F}_{2^8} \)).  
   - Ejemplo para el byte `0x53`:  
     \[
     \text{Inverso}(0x53) = 0xCA \quad \text{(en GF(2⁸))}
     \]  

2. **ShiftRows**:  
   - Desplazamiento cíclico de filas en la matriz de estado.  
   ```plaintext
   Antes:      Después:
   [A B C D]   [A B C D]  
   [E F G H]   [F G H E]  
   [I J K L]   [K L I J]  
   [M N O P]   [P M N O]

   Estado después de AddRoundKey:  
19 3D E3 BE A0 F4 E2 2B 9A C6 8D 2A E9 F8 48 08  

### 📥 **Cómo descargar/convertir a PDF**  
 

2. **Usando Pandoc (local)**:  
   ```bash
   pandoc reporte.md -o reporte.pdf --latex-engine=xelatex -V geometry:margin=1in
