# Enhanced 15-slide generator reflecting the exact user text and layout
import os

html_content = r'''<!DOCTYPE html>
<html lang="es" class="dark scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bosques Aleatorios (Random Forest) | Denshel David Mérida Quispe</title>
  
  <!-- Tailwind CSS v3 via CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          colors: {
            brand: {
              dark: '#030712',
              card: '#0f172a',
              accent: '#34d399',
              cyan: '#22d3ee',
              amber: '#fbbf24',
              rose: '#fb7185'
            }
          },
          fontFamily: {
            sans: ['Inter', 'system-ui', '-apple-system', 'Segoe UI', 'Roboto', 'sans-serif'],
            mono: ['JetBrains Mono', 'Fira Code', 'Menlo', 'Consolas', 'monospace']
          }
        }
      }
    }
  </script>

  <!-- GSAP 3.x via CDN -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
  
  <!-- Chart.js via CDN -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

  <!-- Lucide Icons via CDN -->
  <script src="https://unpkg.com/lucide@latest"></script>

  <style>
    /* Custom Scrollbar & presentation styling */
    ::-webkit-scrollbar {
      width: 6px;
      height: 6px;
    }
    ::-webkit-scrollbar-track {
      background: #020617;
    }
    ::-webkit-scrollbar-thumb {
      background: #334155;
      border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: #10b981;
    }
    .glass-card {
      background: rgba(15, 23, 42, 0.85);
      backdrop-filter: blur(14px);
      border: 1px solid rgba(51, 65, 85, 0.65);
    }
    .glass-card-hover:hover {
      border-color: rgba(52, 211, 153, 0.5);
      box-shadow: 0 0 25px -5px rgba(52, 211, 153, 0.2);
    }
    .text-glow-emerald {
      text-shadow: 0 0 16px rgba(52, 211, 153, 0.5);
    }
    .text-glow-cyan {
      text-shadow: 0 0 16px rgba(34, 211, 238, 0.5);
    }
    .text-glow-amber {
      text-shadow: 0 0 16px rgba(251, 191, 36, 0.5);
    }
    .text-glow-rose {
      text-shadow: 0 0 16px rgba(251, 113, 133, 0.5);
    }
    /* Subtle dot grid background */
    .bg-grid-pattern {
      background-size: 28px 28px;
      background-image: 
        radial-gradient(circle, rgba(71, 85, 105, 0.25) 1px, transparent 1px);
    }
    /* Slide visibility toggle */
    .slide-section {
      display: none;
      opacity: 0;
      width: 100%;
    }
    .slide-section.active {
      display: block;
      opacity: 1;
    }
    .bg-striped-rose {
      background: repeating-linear-gradient(
        45deg,
        rgba(244, 63, 94, 0.15),
        rgba(244, 63, 94, 0.15) 6px,
        rgba(244, 63, 94, 0.3) 6px,
        rgba(244, 63, 94, 0.3) 12px
      );
    }
  </style>
</head>
<body class="bg-slate-950 text-slate-100 font-sans antialiased overflow-x-hidden selection:bg-emerald-500 selection:text-slate-950 min-h-screen flex flex-col justify-between">

  <!-- ==================================================================== -->
  <!-- TOP HEADER / STATUS BAR                                              -->
  <!-- ==================================================================== -->
  <header class="w-full fixed top-0 left-0 z-50 bg-slate-950/90 backdrop-blur-md border-b border-slate-800/90 px-4 md:px-8 py-2.5 flex items-center justify-between">
    <div class="flex items-center gap-3">
      <div class="flex items-center gap-2 px-2.5 py-1 rounded-full bg-emerald-950/80 border border-emerald-500/40 text-emerald-400 text-xs font-mono font-medium tracking-wide">
        <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
        <span>MACHINE LEARNING MASTERCLASS</span>
      </div>
      <span class="text-slate-600 text-xs hidden sm:inline">|</span>
      <h1 class="text-xs md:text-sm font-semibold text-slate-300 tracking-tight hidden sm:block truncate max-w-md">
        Bosques Aleatorios (Random Forest)
      </h1>
    </div>

    <!-- Center Slide Topic Badge -->
    <div id="header-slide-topic" class="text-xs font-mono text-cyan-400 px-3 py-1 rounded-lg bg-slate-900 border border-slate-800 hidden md:block">
      1. Portada
    </div>

    <div class="flex items-center gap-2">
      <!-- Fullscreen Toggle -->
      <button id="btn-fullscreen" title="Pantalla Completa (F)" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 border border-slate-700/60 text-slate-300 hover:text-white transition">
        <i data-lucide="maximize" class="w-4 h-4"></i>
      </button>
      <!-- Shortcuts Help Trigger -->
      <button id="btn-help" title="Atajos de Teclado (?)" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 border border-slate-700/60 text-slate-300 hover:text-white transition">
        <i data-lucide="help-circle" class="w-4 h-4"></i>
      </button>
      <!-- Global Slide Counter in Header -->
      <div class="px-2.5 py-1 rounded-lg bg-slate-900 border border-slate-800 font-mono text-xs text-slate-300">
        <span id="header-counter-current" class="text-emerald-400 font-bold">1</span> / <span id="header-counter-total">15</span>
      </div>
    </div>
  </header>

  <!-- LINEAR PROGRESS BAR -->
  <div class="fixed top-[45px] left-0 w-full h-[3px] bg-slate-900 z-50">
    <div id="progress-bar-fill" class="h-full bg-gradient-to-r from-emerald-500 via-cyan-400 to-emerald-400 w-[6.66%] transition-all duration-300"></div>
  </div>

  <!-- ==================================================================== -->
  <!-- MAIN PRESENTATION VIEWPORT (16:9 Optimized Container)               -->
  <!-- ==================================================================== -->
  <main class="w-full max-w-7xl mx-auto px-4 md:px-8 pt-16 pb-24 flex-grow flex flex-col justify-center relative bg-grid-pattern min-h-[calc(100vh-80px)]">
    
    <!-- ==================================================================== -->
    <!-- SLIDE 1: PORTADA TOTALMENTE LIMPIA Y ELEGANTE                        -->
    <!-- ==================================================================== -->
    <section id="slide-1" class="slide-section active py-12">
      <div class="min-h-[60vh] flex flex-col items-center justify-center text-center space-y-8 relative">
        
        <!-- Subtle Animated Glowing Ambient Circle in Background -->
        <div class="absolute w-96 h-96 bg-emerald-500/10 rounded-full blur-3xl pointer-events-none -z-10 animate-pulse"></div>
        <div class="absolute w-80 h-80 bg-cyan-500/10 rounded-full blur-3xl pointer-events-none -z-10 translate-x-20"></div>

        <!-- Geometric Tree Icon Accent -->
        <div class="w-20 h-20 rounded-2xl bg-slate-900/90 border border-emerald-500/40 flex items-center justify-center shadow-2xl shadow-emerald-500/10 mb-2">
          <svg class="w-12 h-12 text-emerald-400 filter drop-shadow-[0_0_10px_rgba(52,211,153,0.4)]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">
            <polygon points="12 2 4 12 9 12 6 18 18 18 15 12 20 12 12 2" fill="rgba(52,211,153,0.15)"/>
            <rect x="10" y="18" width="4" height="4" fill="#065f46"/>
          </svg>
        </div>

        <!-- Title -->
        <h1 class="text-4xl sm:text-6xl lg:text-7xl font-black tracking-tight text-white leading-tight">
          Bosques Aleatorios<br>
          <span class="bg-gradient-to-r from-emerald-400 via-cyan-300 to-teal-400 bg-clip-text text-transparent text-glow-emerald">
            (Random Forest)
          </span>
        </h1>

        <!-- Author Name (Clean & Prominent) -->
        <div class="pt-4">
          <p class="text-xl sm:text-2xl font-light tracking-widest text-slate-300 font-sans uppercase">
            Denshel David Mérida Quispe
          </p>
          <div class="w-24 h-0.5 bg-gradient-to-r from-transparent via-emerald-400 to-transparent mx-auto mt-4 opacity-75"></div>
        </div>

        <!-- Clean Launch Action Button -->
        <div class="pt-8">
          <button onclick="goToSlide(2)" class="px-6 py-3 rounded-xl bg-slate-900 hover:bg-slate-800 text-emerald-400 border border-emerald-500/40 font-mono text-sm font-semibold tracking-wide flex items-center gap-3 transition transform hover:scale-105 shadow-xl shadow-emerald-950/50">
            <span>Iniciar Presentación</span>
            <i data-lucide="arrow-right" class="w-4 h-4"></i>
          </button>
        </div>

      </div>
    </section>

    <!-- ==================================================================== -->
    <!-- SLIDE 2: CONDORCET (35% TEXTO / 65% SIMULADOR)                      -->
    <!-- ==================================================================== -->
    <section id="slide-2" class="slide-section py-4">
      <div class="space-y-4">
        <!-- Title and Context -->
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-2 border-b border-slate-800 pb-3">
          <div>
            <div class="text-xs font-mono text-cyan-400 uppercase tracking-wider">Fundamento Matemático</div>
            <h2 class="text-2xl md:text-3xl font-extrabold text-white">
              El Fundamento: Teorema del Jurado de Condorcet (1785)
            </h2>
          </div>
          <div class="px-3 py-1.5 rounded-lg bg-cyan-950/60 border border-cyan-500/30 text-cyan-300 font-mono text-xs">
            P<sub>mayoría</sub> = &sum;<sub>k=&lceil;N/2&rceil;</sub><sup>N</sup> (<sup>N</sup><sub>k</sub>) p<sup>k</sup> (1-p)<sup>N-k</sup>
          </div>
        </div>

        <!-- 35% Left / 65% Right Layout -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          
          <!-- LEFT COLUMN (35% width -> ~4.2 cols) -->
          <div class="lg:col-span-4 glass-card p-5 rounded-2xl border border-slate-800 space-y-4">
            <h3 class="text-xs font-mono text-cyan-400 uppercase tracking-wider font-bold flex items-center gap-2">
              <i data-lucide="book-open" class="w-4 h-4"></i>
              Fundamentos Teóricos
            </h3>

            <div class="space-y-3 text-xs text-slate-300 leading-relaxed">
              <p>
                <strong class="text-white text-sm block mb-1">&bull; Premisa:</strong>
                La agregación democrática supera al individuo si cada votante tiene <strong class="text-cyan-300 font-mono">p &gt; 0.50</strong>.
              </p>

              <div class="p-3 rounded-xl bg-slate-900 border border-slate-800 space-y-2">
                <span class="text-[10px] font-mono text-slate-400 uppercase block">&bull; Escala de acierto:</span>
                <ul class="space-y-1.5 text-xs font-mono">
                  <li class="flex justify-between items-center text-slate-300">
                    <span>1 Árbol individual:</span>
                    <strong class="text-slate-100">60.0%</strong>
                  </li>
                  <li class="flex justify-between items-center text-cyan-300">
                    <span>3 Árboles (Mayoría):</span>
                    <strong class="font-bold">64.8%</strong>
                  </li>
                  <li class="flex justify-between items-center text-emerald-400">
                    <span>11 Árboles (Mayoría):</span>
                    <strong class="font-bold text-sm">75.3%</strong>
                  </li>
                </ul>
              </div>

              <div class="p-3 rounded-xl bg-amber-950/30 border border-amber-500/40 text-amber-200 text-xs">
                <strong class="text-amber-300 block mb-1 font-mono">&bull; Condición crítica:</strong>
                Los modelos deben ser <strong class="text-white">estadísticamente independientes</strong>. Errores idénticos anulan el beneficio del ensamble.
              </div>
            </div>
          </div>

          <!-- RIGHT COLUMN (65% width -> ~7.8 cols) -->
          <div class="lg:col-span-8 glass-card p-5 rounded-2xl border border-slate-800 space-y-4">
            
            <div class="flex items-center justify-between">
              <h3 class="text-xs font-mono text-emerald-400 uppercase tracking-wider font-bold flex items-center gap-2">
                <i data-lucide="sliders" class="w-4 h-4"></i>
                Simulador Interactivo de Sliders (p y N)
              </h3>
              <label class="flex items-center gap-2 text-xs font-mono text-rose-300 cursor-pointer">
                <input type="checkbox" id="condorcet-corr-toggle" class="rounded accent-rose-500">
                <span>Error Correlacionado (&rho; = 1)</span>
              </label>
            </div>

            <!-- Sliders -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div class="p-3 bg-slate-900/80 rounded-xl border border-slate-800 space-y-1.5">
                <div class="flex justify-between text-xs font-mono">
                  <span class="text-slate-400">Precisión individual (p):</span>
                  <span id="condorcet-p-val" class="text-cyan-400 font-bold">60.0%</span>
                </div>
                <input type="range" id="condorcet-p-slider" min="0.50" max="0.85" step="0.01" value="0.60" class="w-full accent-cyan-400 cursor-pointer">
                <div class="flex justify-between text-[9px] text-slate-500 font-mono">
                  <span>0.50</span>
                  <span>0.60</span>
                  <span>0.85</span>
                </div>
              </div>

              <div class="p-3 bg-slate-900/80 rounded-xl border border-slate-800 space-y-1.5">
                <div class="flex justify-between text-xs font-mono">
                  <span class="text-slate-400">Número de árboles (N):</span>
                  <span id="condorcet-n-val" class="text-emerald-400 font-bold">11 árboles</span>
                </div>
                <input type="range" id="condorcet-n-slider" min="1" max="25" step="2" value="11" class="w-full accent-emerald-400 cursor-pointer">
                <div class="flex justify-between text-[9px] text-slate-500 font-mono">
                  <span>N = 1</span>
                  <span>N = 11</span>
                  <span>N = 25</span>
                </div>
              </div>
            </div>

            <!-- Giant Metric Display -->
            <div class="p-4 rounded-xl bg-gradient-to-r from-slate-900 via-slate-900/90 to-emerald-950/40 border border-emerald-500/30 flex items-center justify-between">
              <div>
                <span class="text-[11px] font-mono text-slate-400 uppercase">Probabilidad de la Mayoría Colectiva:</span>
                <div class="text-4xl sm:text-5xl font-black text-emerald-400 font-mono text-glow-emerald" id="condorcet-result-metric">
                  75.3%
                </div>
                <div class="text-xs text-slate-400 font-mono mt-1" id="condorcet-subtext">
                  Supera en <span class="text-cyan-300 font-bold">+15.3%</span> la precisión de cualquier árbol individual
                </div>
              </div>
              <div class="text-right">
                <span class="text-[10px] font-mono text-slate-400 block">Mayoría requerida:</span>
                <span class="text-lg font-mono text-cyan-300 font-bold" id="condorcet-majority-req">&ge; 6 de 11 votos</span>
              </div>
            </div>

            <!-- Juror Trees Visual -->
            <div id="condorcet-trees-container" class="grid grid-cols-6 sm:grid-cols-11 gap-1.5 p-3 bg-slate-950/80 rounded-xl border border-slate-800 min-h-[90px] items-center justify-center">
              <!-- Injected via JS -->
            </div>

          </div>

        </div>
      </div>
    </section>

    <!-- ==================================================================== -->
    <!-- SLIDE 3: CASO DE ESTUDIO: CLASIFICACIÓN DE SEÑALES VIALES            -->
    <!-- ==================================================================== -->
    <section id="slide-3" class="slide-section py-4">
      <div class="space-y-4">
        <!-- Title -->
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-2 border-b border-slate-800 pb-3">
          <div>
            <div class="text-xs font-mono text-emerald-400 uppercase tracking-wider">Caso Didáctico</div>
            <h2 class="text-2xl md:text-3xl font-extrabold text-white">
              Caso de Estudio: Clasificación de Señales Viales
            </h2>
          </div>
          <div class="text-xs text-slate-400 font-mono bg-slate-900 px-3 py-1.5 rounded border border-slate-800">
            Espacio de características p = 4
          </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          
          <!-- LEFT COLUMN: Exact Text Bullets (35% -> 4 cols) -->
          <div class="lg:col-span-4 glass-card p-5 rounded-2xl border border-slate-800 space-y-4">
            <h3 class="text-xs font-mono text-emerald-400 uppercase tracking-wider font-bold flex items-center gap-2">
              <i data-lucide="target" class="w-4 h-4"></i>
              Definición del Problema
            </h3>

            <div class="space-y-3 text-xs text-slate-300 leading-relaxed">
              <p>
                <strong class="text-white block mb-1">&bull; Objetivo:</strong>
                Clasificar si una señal corresponde a un <strong class="text-emerald-400 font-mono">Cruce Peatonal (Sí / No)</strong>.
              </p>

              <div class="p-3 rounded-xl bg-slate-900 border border-slate-800 space-y-1.5">
                <span class="text-[10px] font-mono text-slate-400 uppercase block">&bull; Espacio de características (p = 4):</span>
                <ul class="space-y-1 text-slate-300 font-mono text-[11px]">
                  <li><strong class="text-cyan-300">Tamaño:</strong> Pequeño, Mediano o Grande.</li>
                  <li><strong class="text-cyan-300">Forma:</strong> 3 lados, 4 lados, 8 lados o Círculo.</li>
                  <li><strong class="text-cyan-300">Colores:</strong> Monocromático, Bicolor o Multicolor.</li>
                  <li><strong class="text-cyan-300">Contenido:</strong> Presencia de texto o símbolo puro.</li>
                </ul>
              </div>

              <div class="p-3 rounded-xl bg-rose-950/30 border border-rose-500/40 text-xs text-rose-200">
                <strong class="text-rose-400 block mb-1 font-mono">&bull; Falla del árbol único:</strong>
                Sobreajuste y rigidez ante variantes no vistas (ej. carteles circulares).
              </div>
            </div>
          </div>

          <!-- RIGHT COLUMN: Interactive Cards + Visual Sign (65% -> 8 cols) -->
          <div class="lg:col-span-8 glass-card p-5 rounded-2xl border border-slate-800 space-y-4">
            
            <div class="flex items-center justify-between">
              <span class="text-xs font-mono text-slate-300 font-bold">Configuración Interactiva del Cartel</span>
              <button onclick="loadSignEdgeCase()" class="text-xs px-2.5 py-1 rounded bg-amber-950/60 hover:bg-amber-900 border border-amber-500/50 text-amber-300 font-mono">
                Cargar Caso Límite (Circular) &rarr;
              </button>
            </div>

            <!-- 4 Feature Selectors -->
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
              <!-- Size -->
              <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 space-y-1">
                <span class="text-[10px] font-mono text-slate-400 block">Tamaño:</span>
                <select id="feat-size" onchange="onSignSelectorChange()" class="w-full bg-slate-950 border border-slate-700 text-slate-200 rounded p-1 text-xs font-mono">
                  <option value="Grande">Grande</option>
                  <option value="Mediano" selected>Mediano</option>
                  <option value="Pequeño">Pequeño</option>
                </select>
              </div>
              <!-- Shape -->
              <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 space-y-1">
                <span class="text-[10px] font-mono text-slate-400 block">Forma (Caras):</span>
                <select id="feat-shape" onchange="onSignSelectorChange()" class="w-full bg-slate-950 border border-slate-700 text-slate-200 rounded p-1 text-xs font-mono">
                  <option value="Triángulo (3)" selected>3 lados (Triáng)</option>
                  <option value="Rombo (4)">4 lados (Rombo)</option>
                  <option value="Octágono (8)">8 lados (Octág)</option>
                  <option value="Círculo (1)">Círculo</option>
                </select>
              </div>
              <!-- Colors -->
              <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 space-y-1">
                <span class="text-[10px] font-mono text-slate-400 block">Colores:</span>
                <select id="feat-color" onchange="onSignSelectorChange()" class="w-full bg-slate-950 border border-slate-700 text-slate-200 rounded p-1 text-xs font-mono">
                  <option value="Monocromo">Monocromático</option>
                  <option value="Bicolor" selected>Bicolor</option>
                  <option value="Multicolor">Multicolor</option>
                </select>
              </div>
              <!-- Content -->
              <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 space-y-1">
                <span class="text-[10px] font-mono text-slate-400 block">Contenido:</span>
                <select id="feat-content" onchange="onSignSelectorChange()" class="w-full bg-slate-950 border border-slate-700 text-slate-200 rounded p-1 text-xs font-mono">
                  <option value="Persona" selected>Símbolo Peatón</option>
                  <option value="Texto">Texto ("STOP/CEDA")</option>
                </select>
              </div>
            </div>

            <!-- Visual Preview & Side-by-Side Model Verdict -->
            <div class="grid grid-cols-1 sm:grid-cols-12 gap-4 items-center pt-2">
              <div class="sm:col-span-4 flex flex-col items-center justify-center p-3 rounded-xl bg-slate-950 border border-slate-800">
                <div id="sign-svg-wrapper" class="w-20 h-20 flex items-center justify-center"></div>
                <span id="sign-summary-text" class="text-[10px] font-mono text-cyan-300 mt-2 text-center">Mediano • 3 Lados • Bicolor • Peatón</span>
              </div>

              <div class="sm:col-span-8 space-y-3">
                <!-- Single Tree -->
                <div class="p-2.5 rounded-lg bg-rose-950/20 border border-rose-500/30 flex items-center justify-between">
                  <div>
                    <span class="text-xs font-mono text-rose-400 font-bold block">Árbol Único (Rígido):</span>
                    <span class="text-[10px] text-slate-400 font-mono">Regla fija memorizada: IF Forma == Triángulo AND Peatón</span>
                  </div>
                  <span id="single-tree-verdict" class="text-xs font-mono font-bold px-2 py-1 rounded bg-emerald-950 text-emerald-400 border border-emerald-500/40">
                    SÍ (CRUCE)
                  </span>
                </div>

                <!-- Random Forest -->
                <div class="p-2.5 rounded-lg bg-emerald-950/20 border border-emerald-500/40 flex items-center justify-between">
                  <div>
                    <span class="text-xs font-mono text-emerald-400 font-bold block">Random Forest (5 Árboles):</span>
                    <span class="text-[10px] text-slate-400 font-mono">Consenso de 5 árboles evaluando subconjuntos distintos</span>
                  </div>
                  <span id="forest-verdict" class="text-xs font-mono font-bold px-2 py-1 rounded bg-emerald-950 text-emerald-400 border border-emerald-500/40">
                    SÍ (4/5 Votos)
                  </span>
                </div>
              </div>
            </div>

          </div>

        </div>
      </div>
    </section>

    <!-- ==================================================================== -->
    <!-- SLIDE 4: DOBLE ALEATORIEDAD - PASO 1: BAGGING                       -->
    <!-- ==================================================================== -->
    <section id="slide-4" class="slide-section py-4">
      <div class="space-y-4">
        <!-- Title -->
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-2 border-b border-slate-800 pb-3">
          <div>
            <div class="text-xs font-mono text-amber-400 uppercase tracking-wider">Leo Breiman (2001) &bull; Pilar 1</div>
            <h2 class="text-2xl md:text-3xl font-extrabold text-white">
              Doble Aleatoriedad: 1. Bagging (Bootstrap Aggregating)
            </h2>
          </div>
          <div class="text-xs font-mono text-emerald-300 bg-emerald-950 px-3 py-1.5 rounded border border-emerald-500/40">
            Muestreo de Filas con Reemplazo
          </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          <!-- Left: Exact Theory Text -->
          <div class="lg:col-span-5 glass-card p-5 rounded-2xl border border-slate-800 space-y-4">
            <h3 class="text-xs font-mono text-emerald-400 uppercase tracking-wider font-bold flex items-center gap-2">
              <i data-lucide="layers" class="w-4 h-4"></i>
              Fundamento de Bagging
            </h3>

            <div class="space-y-3 text-xs text-slate-300 leading-relaxed">
              <p>
                <strong class="text-white block mb-1">&bull; Muestreo con reemplazo de tamaño N:</strong>
                Genera datasets únicos por cada árbol individual a partir del mismo conjunto original.
              </p>

              <div class="p-3.5 rounded-xl bg-slate-900 border border-cyan-500/30 space-y-2">
                <span class="text-[11px] font-mono text-cyan-300 font-bold block">&bull; Validación Out-of-Bag (OOB):</span>
                <p class="text-slate-300 text-xs">
                  Aproximadamente el <strong class="text-emerald-400 font-mono">&approx; 36.8%</strong> de las muestras queda fuera como conjunto de validación OOB:
                </p>
                <div class="p-2 rounded bg-slate-950 font-mono text-xs text-center border border-slate-800 text-cyan-300">
                  lim<sub>N&rarr;&infin;</sub> (1 - 1/N)<sup>N</sup> = 1/e &approx; <strong>36.79%</strong>
                </div>
                <p class="text-[11px] text-slate-400">
                  Permite evaluar el error de generalización sin requerir validación cruzada externa costosa.
                </p>
              </div>

              <button onclick="generateBootstrapSample()" class="w-full py-2.5 rounded-xl bg-gradient-to-r from-emerald-500 to-teal-600 hover:from-emerald-400 text-slate-950 font-bold text-xs font-mono flex items-center justify-center gap-2 shadow-lg shadow-emerald-500/20 transition">
                <i data-lucide="dice-5" class="w-4 h-4"></i>
                <span>Generar Nueva Muestra Bootstrap</span>
              </button>
            </div>
          </div>

          <!-- Right: Visual Simulation Table -->
          <div class="lg:col-span-7 glass-card p-5 rounded-2xl border border-slate-800 space-y-3">
            <div class="flex items-center justify-between text-xs font-mono font-bold">
              <span class="text-slate-300">Dataset Original (N = 10)</span>
              <span class="text-slate-400">Muestra Bootstrap Generada:</span>
            </div>

            <div class="grid grid-cols-2 gap-3">
              <div class="space-y-1" id="s4-original-list"></div>
              <div class="space-y-1" id="s4-bootstrap-list"></div>
            </div>

            <div class="flex items-center justify-between pt-2 border-t border-slate-800 text-xs font-mono">
              <span class="text-emerald-400 font-bold" id="s4-inbag-count">6 únicas (10 con reemplazo)</span>
              <span class="text-rose-400 font-bold" id="s4-oob-count">4 muestras OOB (40%)</span>
            </div>
          </div>
        </div>

      </div>
    </section>

    <!-- ==================================================================== -->
    <!-- SLIDE 5: DOBLE ALEATORIEDAD - PASO 2: RANDOM SUBSPACE                -->
    <!-- ==================================================================== -->
    <section id="slide-5" class="slide-section py-4">
      <div class="space-y-4">
        <!-- Title -->
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-2 border-b border-slate-800 pb-3">
          <div>
            <div class="text-xs font-mono text-cyan-400 uppercase tracking-wider">Leo Breiman (2001) &bull; Pilar 2</div>
            <h2 class="text-2xl md:text-3xl font-extrabold text-white">
              Doble Aleatoriedad: 2. Subespacio Aleatorio (Feature Selection)
            </h2>
          </div>
          <div class="text-xs font-mono text-cyan-300 bg-cyan-950 px-3 py-1.5 rounded border border-cyan-500/40">
            Muestreo de Columnas en cada Nodo
          </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          <!-- Left: Exact Theory Text -->
          <div class="lg:col-span-5 glass-card p-5 rounded-2xl border border-slate-800 space-y-4">
            <h3 class="text-xs font-mono text-cyan-400 uppercase tracking-wider font-bold flex items-center gap-2">
              <i data-lucide="columns" class="w-4 h-4"></i>
              Fundamento del Subespacio
            </h3>

            <div class="space-y-3 text-xs text-slate-300 leading-relaxed">
              <p>
                <strong class="text-white block mb-1">&bull; Subconjunto aleatorio en cada división:</strong>
                En cada división de nodo se evalúa solo un subconjunto aleatorio de variables:
                <span class="text-cyan-300 font-mono font-bold block mt-1 text-sm">m &approx; &radic;p &nbsp;(para p = 4 &rarr; m = 2)</span>
              </p>

              <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2 text-xs">
                <span class="text-[10px] font-mono text-slate-400 uppercase block">&bull; Mecanismo descorrelacionador:</span>
                <p class="text-slate-300">
                  Evita que variables dominantes monopolicen los nodos raíz y descorrelaciona los árboles.
                </p>
                <p class="text-slate-400 text-[11px]">
                  Si no se ocultaran variables, todos los árboles elegirían la misma variable en la raíz, destruyendo la independencia de Condorcet.
                </p>
              </div>

              <button onclick="simulateNodeSplit()" class="w-full py-2.5 rounded-xl bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 text-slate-950 font-bold text-xs font-mono flex items-center justify-center gap-2 shadow-lg shadow-cyan-500/20 transition">
                <i data-lucide="shuffle" class="w-4 h-4"></i>
                <span>Simular División en un Nuevo Nodo</span>
              </button>
            </div>
          </div>

          <!-- Right: Visual Simulation Grid -->
          <div class="lg:col-span-7 glass-card p-5 rounded-2xl border border-slate-800 space-y-4">
            <div class="flex items-center justify-between text-xs font-mono font-bold">
              <span class="text-slate-300">Variables Totales Disponibles (p = 4):</span>
              <span class="text-cyan-400">Subespacio m = &radic;4 = 2 seleccionadas</span>
            </div>

            <div class="grid grid-cols-2 sm:grid-cols-4 gap-2.5" id="s5-features-subspace-container">
              <!-- Populated via JS -->
            </div>

            <!-- Decision branch visualization -->
            <div class="p-4 rounded-xl bg-slate-950 border border-slate-800 flex flex-col items-center">
              <span class="text-[11px] font-mono text-slate-400 mb-2">Nodo de Decisión Activo:</span>
              <div id="s5-active-split-badge" class="px-3 py-1 rounded-lg bg-cyan-950 border border-cyan-500 text-cyan-300 text-xs font-mono font-bold">
                Buscando mejor división entre: [Tamaño] y [Caras]
              </div>
              <div class="flex gap-16 mt-3 text-xs font-mono">
                <div class="text-center text-emerald-400">&larr; Umbral SÍ (Izquierda)</div>
                <div class="text-center text-rose-400">Umbral NO (Derecha) &rarr;</div>
              </div>
            </div>
          </div>
        </div>

      </div>
    </section>

    <!-- ==================================================================== -->
    <!-- SLIDE 6: DESCORRELACIÓN Y REDUCCIÓN DE VARIANZA - TEORÍA            -->
    <!-- ==================================================================== -->
    <section id="slide-6" class="slide-section py-4">
      <div class="space-y-4">
        <!-- Title -->
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-2 border-b border-slate-800 pb-3">
          <div>
            <div class="text-xs font-mono text-cyan-400 uppercase tracking-wider">Fundamento Teórico</div>
            <h2 class="text-2xl md:text-3xl font-extrabold text-white">
              Descorrelación y Reducción de Varianza
            </h2>
          </div>
          <div class="text-xs font-mono text-emerald-300 bg-emerald-950 px-3 py-1.5 rounded border border-emerald-500/40">
            Var(Ensemble) = &rho;&sigma;² + [(1 - &rho;) / B] &sigma;²
          </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          
          <!-- Left: Exact Theory Text -->
          <div class="lg:col-span-6 glass-card p-5 rounded-2xl border border-slate-800 space-y-4">
            <h3 class="text-xs font-mono text-cyan-400 uppercase tracking-wider font-bold flex items-center gap-2">
              <i data-lucide="shield" class="w-4 h-4"></i>
              Principios Rectores
            </h3>

            <div class="space-y-3 text-xs text-slate-300 leading-relaxed">
              <p>
                <strong class="text-white block mb-1">&bull; Principio rector:</strong>
                Menor correlación entre clasificadores = Menor error de generalización.
              </p>

              <!-- Exact Formula Card -->
              <div class="p-4 rounded-xl bg-slate-900 border border-emerald-500/40 space-y-2">
                <span class="text-[10px] font-mono text-slate-400 uppercase block">&bull; Fórmula del balance:</span>
                <div class="text-lg sm:text-xl font-bold font-mono text-emerald-400 text-center py-1">
                  Var(Ensemble) &approx; &rho;&sigma;<sup>2</sup> + <sup>(1 - &rho;)</sup>&frasl;<sub>B</sub> &sigma;<sup>2</sup>
                </div>
              </div>

              <div class="p-3 rounded-xl bg-slate-900 border border-slate-800 space-y-2">
                <span class="text-[10px] font-mono text-slate-400 uppercase block">&bull; Efecto colectivo:</span>
                <ul class="space-y-1.5 text-slate-300">
                  <li>&bull; Si <strong class="text-cyan-300 font-mono">B &rarr; &infin;</strong>, el segundo término desaparece; el error queda acotado por la correlación <strong class="text-amber-300 font-mono">&rho;</strong>.</li>
                  <li>&bull; Los árboles fallan en muestras distintas; el voto mayoritario cancela el error residual.</li>
                </ul>
              </div>
            </div>
          </div>

          <!-- Right: Interactive Variance Calculator Simulator -->
          <div class="lg:col-span-6 glass-card p-5 rounded-2xl border border-slate-800 space-y-4">
            <h3 class="text-xs font-mono text-emerald-400 uppercase tracking-wider font-bold flex items-center gap-2">
              <i data-lucide="gauge" class="w-4 h-4"></i>
              Simulador de Varianza según &rho; y B
            </h3>

            <!-- Sliders for rho and B -->
            <div class="space-y-3">
              <div class="p-3 bg-slate-900 rounded-xl border border-slate-800 space-y-1">
                <div class="flex justify-between text-xs font-mono">
                  <span class="text-slate-400">Correlación entre árboles (&rho;):</span>
                  <span id="var-rho-val" class="text-amber-400 font-bold">0.20</span>
                </div>
                <input type="range" id="var-rho-slider" min="0.0" max="1.0" step="0.05" value="0.20" class="w-full accent-amber-400 cursor-pointer">
              </div>

              <div class="p-3 bg-slate-900 rounded-xl border border-slate-800 space-y-1">
                <div class="flex justify-between text-xs font-mono">
                  <span class="text-slate-400">Número de árboles (B):</span>
                  <span id="var-b-val" class="text-emerald-400 font-bold">100 árboles</span>
                </div>
                <input type="range" id="var-b-slider" min="1" max="200" step="1" value="100" class="w-full accent-emerald-400 cursor-pointer">
              </div>
            </div>

            <!-- Variance Breakdown Visual -->
            <div class="p-4 rounded-xl bg-slate-950 border border-slate-800 space-y-3">
              <div class="flex justify-between items-center text-xs font-mono">
                <span class="text-slate-400">Varianza Total del Ensamble:</span>
                <span id="var-total-val" class="text-emerald-400 font-bold text-lg">0.208 &sigma;²</span>
              </div>
              <div class="w-full h-3 bg-slate-800 rounded-full overflow-hidden flex">
                <div id="var-bar-irreducible" class="bg-amber-400 h-full transition-all duration-300" style="width: 20%;" title="Piso Irreducible (rho * sigma^2)"></div>
                <div id="var-bar-reducible" class="bg-cyan-400 h-full transition-all duration-300" style="width: 0.8%;" title="Término Reducible ((1-rho)/B * sigma^2)"></div>
              </div>
              <div class="flex justify-between text-[10px] font-mono">
                <span class="text-amber-400">&bull; Piso Irreducible (&rho;&sigma;²): <strong id="var-irred-val">0.20 &sigma;²</strong></span>
                <span class="text-cyan-400">&bull; Reducible: <strong id="var-red-val">0.008 &sigma;²</strong></span>
              </div>
            </div>

            <div class="text-[11px] font-mono text-slate-400 bg-slate-900/60 p-2.5 rounded-lg border border-slate-800">
              Insight: Añadir más árboles disminuye la varianza reducible a cero, pero jamás podrá reducir el piso marcado por la correlación residual &rho;.
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- ==================================================================== -->
    <!-- SLIDE 7: DESCORRELACIÓN - MATRIZ DE PREDICCIONES (9 x 6)            -->
    <!-- ==================================================================== -->
    <section id="slide-7" class="slide-section py-4">
      <div class="space-y-4">
        <!-- Title -->
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-2 border-b border-slate-800 pb-3">
          <div>
            <div class="text-xs font-mono text-emerald-400 uppercase tracking-wider">Demostración Empírica</div>
            <h2 class="text-2xl md:text-3xl font-extrabold text-white">
              Cancelación del Error Residual: Matriz de 9 Árboles &times; 6 Señales
            </h2>
          </div>
          <div class="text-xs font-mono text-emerald-300 bg-emerald-950 px-3 py-1.5 rounded border border-emerald-500/40">
            "Los árboles fallan en muestras distintas; el voto mayoritario cancela el error"
          </div>
        </div>

        <!-- Matrix Card -->
        <div class="glass-card p-5 rounded-2xl border border-slate-800 space-y-4">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 text-xs font-mono">
            <span class="text-slate-300 font-bold">
              Cuadrícula de 9 Árboles (Filas) evaluando 6 Señales de Prueba (Columnas)
            </span>
            <div class="flex items-center gap-3">
              <span class="flex items-center gap-1 text-emerald-400"><span class="w-2.5 h-2.5 rounded-full bg-emerald-400"></span> Acierto</span>
              <span class="flex items-center gap-1 text-rose-400"><span class="w-2.5 h-2.5 rounded-full bg-rose-500"></span> Fallo Individual</span>
            </div>
          </div>

          <!-- Table -->
          <div class="overflow-x-auto">
            <table class="w-full text-center text-xs font-mono border-collapse" id="mlu-matrix-table">
              <thead>
                <tr class="border-b border-slate-800 text-slate-400">
                  <th class="py-2 px-3 text-left">Modelo</th>
                  <th class="py-2 px-2">Señal 1</th>
                  <th class="py-2 px-2">Señal 2</th>
                  <th class="py-2 px-2">Señal 3</th>
                  <th class="py-2 px-2">Señal 4</th>
                  <th class="py-2 px-2">Señal 5</th>
                  <th class="py-2 px-2">Señal 6</th>
                  <th class="py-2 px-3 text-right">Precisión</th>
                </tr>
              </thead>
              <tbody id="mlu-matrix-body" class="divide-y divide-slate-800/60"></tbody>
              <tfoot id="mlu-matrix-foot" class="border-t-2 border-emerald-500/50 bg-emerald-950/30"></tfoot>
            </table>
          </div>

          <div class="text-[11px] text-slate-400 font-mono flex items-center justify-between pt-1">
            <span>&bull; Haz clic en cualquier celda para alternar acierto/error y ver la resiliencia del consenso colectivo.</span>
            <button onclick="resetMLUMatrix()" class="text-cyan-400 hover:underline">Restablecer Matriz</button>
          </div>
        </div>

      </div>
    </section>

    <!-- ==================================================================== -->
    <!-- SLIDE 8: AUDITORÍA CON XAI: SUPERANDO A GINI CON SHAP                -->
    <!-- ==================================================================== -->
    <section id="slide-8" class="slide-section py-4">
      <div class="space-y-4">
        <!-- Title -->
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-2 border-b border-slate-800 pb-3">
          <div>
            <div class="text-xs font-mono text-rose-400 uppercase tracking-wider">Aporte Crítico 1: Explicabilidad</div>
            <h2 class="text-2xl md:text-3xl font-extrabold text-white">
              Auditoría con XAI: Superando a Gini con SHAP
            </h2>
          </div>
          <div class="text-xs font-mono text-cyan-300 bg-cyan-950 px-3 py-1.5 rounded border border-cyan-500/40">
            TreeSHAP: Algoritmo Polinomial O(TLD²)
          </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          
          <!-- Left: Exact Theory Bullets -->
          <div class="lg:col-span-5 glass-card p-5 rounded-2xl border border-slate-800 space-y-4">
            <h3 class="text-xs font-mono text-rose-400 uppercase tracking-wider font-bold flex items-center gap-2">
              <i data-lucide="alert-triangle" class="w-4 h-4"></i>
              Fundamentos Críticos
            </h3>

            <div class="space-y-3 text-xs text-slate-300 leading-relaxed">
              <div class="p-3 rounded-xl bg-rose-950/20 border border-rose-500/30">
                <strong class="text-rose-400 block mb-1 font-mono">&bull; Límite de Gini (MDI):</strong>
                Mide magnitud de importancia, pero no indica si una variable sube o baja la probabilidad de predicción.
              </div>

              <div class="p-3 rounded-xl bg-emerald-950/20 border border-emerald-500/30">
                <strong class="text-emerald-400 block mb-1 font-mono">&bull; Valores de Shapley (SHAP):</strong>
                Descomponen el aporte aditivo neto (<strong class="text-white">&phi;<sub>i</sub></strong>) por variable y por muestra:
                <div class="p-2 rounded bg-slate-950 border border-slate-800 text-center font-mono text-cyan-300 my-1">
                  &fnof;(x) = E[&fnof;(X)] + &sum; &phi;<sub>i</sub>
                </div>
              </div>

              <div class="p-3 rounded-xl bg-slate-900 border border-slate-800 space-y-1">
                <strong class="text-white block font-mono">&bull; Hallazgo empírico:</strong>
                <ul class="space-y-1 text-slate-400 text-[11px]">
                  <li>- Puntos rojos (valores altos) de <em>concavidad</em> o <em>perímetro</em> desplazan la predicción hacia malignidad.</li>
                  <li>- Permite auditar sesgos y validar decisiones críticas en salud y finanzas.</li>
                </ul>
              </div>
            </div>
          </div>

          <!-- Right: Visual Comparison Cards -->
          <div class="lg:col-span-7 glass-card p-5 rounded-2xl border border-slate-800 space-y-4">
            <h3 class="text-xs font-mono text-slate-300 uppercase tracking-wider font-bold flex items-center gap-2">
              <i data-lucide="git-commit" class="w-4 h-4 text-cyan-400"></i>
              Comparativa de Métodos de Auditoría
            </h3>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
              <div class="p-4 rounded-xl bg-slate-900 border border-rose-500/30 space-y-2">
                <span class="text-xs font-mono font-bold text-rose-400 block">Gini MDI (Scikit-Learn)</span>
                <ul class="text-slate-400 text-xs space-y-1">
                  <li>&cross; Sin signo (solo magnitud bruta).</li>
                  <li>&cross; Fuerte sesgo hacia variables continuas ruidosas con muchos cortes.</li>
                  <li>&cross; Inconsistente ante variables correlacionadas.</li>
                </ul>
              </div>

              <div class="p-4 rounded-xl bg-slate-900 border border-emerald-500/40 space-y-2">
                <span class="text-xs font-mono font-bold text-emerald-400 block">Valores de Shapley (TreeSHAP)</span>
                <ul class="text-slate-300 text-xs space-y-1">
                  <li>&check; Direccional (positivo o negativo).</li>
                  <li>&check; Garantía teórica de eficiencia y simetría.</li>
                  <li>&check; Explicaciones locales y globales consistentes.</li>
                </ul>
              </div>
            </div>

            <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 flex items-center justify-between">
              <span class="text-xs font-mono text-slate-400">Pasa a la siguiente diapositiva para explorar el Beeswarm Plot interactivo:</span>
              <button onclick="goToSlide(9)" class="px-3 py-1.5 rounded-lg bg-cyan-950 hover:bg-cyan-900 border border-cyan-500/40 text-cyan-300 font-mono text-xs flex items-center gap-1.5 transition">
                <span>Ver Beeswarm Plot</span>
                <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
              </button>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- ==================================================================== -->
    <!-- SLIDE 9: GRÁFICO SHAP BEESWARM INTERACTIVO                           -->
    <!-- ==================================================================== -->
    <section id="slide-9" class="slide-section py-4">
      <div class="space-y-4">
        <!-- Title -->
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-2 border-b border-slate-800 pb-3">
          <div>
            <div class="text-xs font-mono text-rose-400 uppercase tracking-wider">Laboratorio Interactivo XAI</div>
            <h2 class="text-2xl md:text-3xl font-extrabold text-white">
              Gráfico de Dispersión SHAP (Beeswarm Plot)
            </h2>
          </div>
          <div class="flex items-center gap-2">
            <div class="flex items-center gap-1 bg-slate-900 p-1 rounded-lg border border-slate-800 text-[10px] font-mono">
              <button onclick="filterShapPoints('all')" class="px-2 py-0.5 rounded bg-slate-800 text-slate-200" id="shap-btn-all">Todos</button>
              <button onclick="filterShapPoints('high')" class="px-2 py-0.5 rounded text-rose-400 hover:bg-slate-800" id="shap-btn-high">Rojos (Altos)</button>
              <button onclick="filterShapPoints('low')" class="px-2 py-0.5 rounded text-blue-400 hover:bg-slate-800" id="shap-btn-low">Azules (Bajos)</button>
            </div>
          </div>
        </div>

        <!-- Beeswarm Container -->
        <div class="glass-card p-5 rounded-2xl border border-slate-800 space-y-4">
          <div class="flex items-center justify-between text-xs font-mono">
            <span class="text-slate-300 font-bold">Pasa el cursor sobre los puntos para auditar el aporte aditivo &phi;<sub>i</sub></span>
            <div class="flex items-center gap-2 text-[10px]">
              <span class="text-blue-400">Valor Bajo</span>
              <div class="w-20 h-2 rounded bg-gradient-to-r from-blue-500 via-purple-500 to-rose-500"></div>
              <span class="text-rose-400">Valor Alto</span>
            </div>
          </div>

          <div class="relative w-full h-72 bg-slate-950/90 rounded-xl border border-slate-800 p-3 overflow-hidden flex flex-col justify-between" id="shap-beeswarm-container">
            <!-- Center zero line -->
            <div class="absolute left-1/2 top-0 bottom-0 w-[1px] bg-slate-700/80 z-0"></div>

            <div class="relative z-10 space-y-4 py-2" id="shap-features-rows">
              <div class="flex items-center text-xs font-mono">
                <span class="w-44 text-right pr-3 text-slate-300 truncate">worst concave points</span>
                <div class="relative flex-1 h-8 bg-slate-900/40 rounded flex items-center shap-row" data-feature="worst concave points"></div>
              </div>
              <div class="flex items-center text-xs font-mono">
                <span class="w-44 text-right pr-3 text-slate-300 truncate">worst perimeter</span>
                <div class="relative flex-1 h-8 bg-slate-900/40 rounded flex items-center shap-row" data-feature="worst perimeter"></div>
              </div>
              <div class="flex items-center text-xs font-mono">
                <span class="w-44 text-right pr-3 text-slate-300 truncate">mean radius</span>
                <div class="relative flex-1 h-8 bg-slate-900/40 rounded flex items-center shap-row" data-feature="mean radius"></div>
              </div>
              <div class="flex items-center text-xs font-mono">
                <span class="w-44 text-right pr-3 text-slate-300 truncate text-slate-500">texture error (ruido)</span>
                <div class="relative flex-1 h-8 bg-slate-900/40 rounded flex items-center shap-row" data-feature="texture error"></div>
              </div>
            </div>

            <div class="flex justify-between text-[10px] font-mono text-slate-500 px-44 border-t border-slate-800/80 pt-1">
              <span>&larr; Empuja a Clase Negativa (&phi; < 0)</span>
              <span class="text-cyan-400 font-bold">&phi; = 0.0</span>
              <span>Empuja a Clase Positiva (&phi; > 0) &rarr;</span>
            </div>

            <!-- Floating Tooltip -->
            <div id="shap-tooltip" class="absolute hidden z-30 p-2.5 rounded-lg bg-slate-900/95 border border-cyan-500/50 text-slate-200 text-xs font-mono shadow-2xl pointer-events-none"></div>
          </div>
        </div>

      </div>
    </section>

    <!-- ==================================================================== -->
    <!-- SLIDE 10: LÍMITE MATEMÁTICO: FALLO DE EXTRAPOLACIÓN (TEORÍA)         -->
    <!-- ==================================================================== -->
    <section id="slide-10" class="slide-section py-4">
      <div class="space-y-4">
        <!-- Title -->
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-2 border-b border-slate-800 pb-3">
          <div>
            <div class="text-xs font-mono text-rose-400 uppercase tracking-wider">Aporte Crítico 2: Límite Matemático</div>
            <h2 class="text-2xl md:text-3xl font-extrabold text-white">
              Límite Matemático: Fallo de Extrapolación
            </h2>
          </div>
          <div class="text-xs font-mono text-rose-300 bg-rose-950 px-3 py-1.5 rounded border border-rose-500/40">
            Incapacidad Estricta de Proyectar Tendencias
          </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          
          <!-- Left: Exact Theory Text -->
          <div class="lg:col-span-5 glass-card p-5 rounded-2xl border border-slate-800 space-y-4">
            <h3 class="text-xs font-mono text-rose-400 uppercase tracking-wider font-bold flex items-center gap-2">
              <i data-lucide="alert-octagon" class="w-4 h-4"></i>
              Fundamento Analítico
            </h3>

            <div class="space-y-3 text-xs text-slate-300 leading-relaxed">
              <p>
                <strong class="text-white block mb-1">&bull; Partición del espacio:</strong>
                Los árboles dividen el espacio en hiperrectángulos ortogonales cerrados alineados con los ejes de las variables.
              </p>

              <p>
                <strong class="text-white block mb-1">&bull; Salida en nodos hoja:</strong>
                Son promedios estáticos constantes de los datos de entrenamiento observados que cayeron en dicha partición.
              </p>

              <div class="p-3 rounded-xl bg-rose-950/20 border border-rose-500/30 space-y-1.5">
                <strong class="text-rose-400 block font-mono">&bull; Falla en el futuro (X &gt; X<sub>max</sub>):</strong>
                <ul class="space-y-1 text-slate-300 text-xs">
                  <li>- Incapaz de proyectar tendencias continuas fuera del rango histórico.</li>
                  <li>- El modelo se aplana en una línea horizontal constante: <strong class="text-white font-mono">&fnof;(x) &le; max(Y<sub>train</sub>)</strong>.</li>
                </ul>
              </div>

              <div class="p-3 rounded-xl bg-amber-950/30 border border-amber-500/40 text-xs text-amber-200">
                <strong class="text-amber-300 block mb-1 font-mono">&bull; Criterio técnico:</strong>
                Nunca usar directamente sobre series temporales con tendencia sin diferenciar los datos previamente.
              </div>
            </div>
          </div>

          <!-- Right: Visual Orthogonal Hypercube Diagram -->
          <div class="lg:col-span-7 glass-card p-5 rounded-2xl border border-slate-800 space-y-4">
            <h3 class="text-xs font-mono text-slate-300 uppercase tracking-wider font-bold flex items-center gap-2">
              <i data-lucide="box" class="w-4 h-4 text-rose-400"></i>
              Demostración Geométrica de las Particiones Ortogonales
            </h3>

            <!-- SVG Orthogonal Partition Diagram -->
            <div class="p-4 bg-slate-950 rounded-xl border border-slate-800 flex flex-col items-center justify-center">
              <svg class="w-72 h-44" viewBox="0 0 300 180">
                <!-- Training Region Box -->
                <rect x="30" y="30" width="160" height="120" fill="rgba(34, 211, 238, 0.08)" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,4"/>
                <text x="110" y="22" font-size="10" font-family="monospace" fill="#38bdf8" text-anchor="middle">Región de Entrenamiento [0, Xmax]</text>
                
                <!-- Internal Splits -->
                <line x1="110" y1="30" x2="110" y2="150" stroke="#475569" stroke-width="1.5"/>
                <line x1="30" y1="90" x2="110" y2="90" stroke="#475569" stroke-width="1.5"/>
                
                <!-- Leaves -->
                <text x="70" y="65" font-size="9" font-family="monospace" fill="#94a3b8" text-anchor="middle">Hoja 1 (ȳ = 4)</text>
                <text x="70" y="125" font-size="9" font-family="monospace" fill="#94a3b8" text-anchor="middle">Hoja 2 (ȳ = 8)</text>
                <text x="150" y="95" font-size="9" font-family="monospace" fill="#34d399" font-weight="bold" text-anchor="middle">Hoja Max (ȳ = 18)</text>

                <!-- Extrapolation Danger Zone -->
                <rect x="190" y="30" width="90" height="120" fill="rgba(244, 63, 94, 0.12)" stroke="#f43f5e" stroke-width="2"/>
                <text x="235" y="80" font-size="9" font-family="monospace" fill="#f43f5e" font-weight="bold" text-anchor="middle">ZONA FUTURA</text>
                <text x="235" y="95" font-size="8" font-family="monospace" fill="#fda4af" text-anchor="middle">(X > Xmax)</text>
                <text x="235" y="115" font-size="8" font-family="monospace" fill="#fda4af" text-anchor="middle">Cae en Hoja Max</text>
                <text x="235" y="128" font-size="8" font-family="monospace" fill="#fb7185" font-weight="bold" text-anchor="middle">ŷ = 18 (Plana)</text>
              </svg>
            </div>

            <div class="text-right">
              <button onclick="goToSlide(11)" class="px-3.5 py-1.5 rounded-lg bg-rose-950 hover:bg-rose-900 border border-rose-500/40 text-rose-300 font-mono text-xs inline-flex items-center gap-1.5 transition">
                <span>Ver Gráfico Comparativo en Vivo (Chart.js)</span>
                <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
              </button>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- ==================================================================== -->
    <!-- SLIDE 11: GRÁFICO DINÁMICO DE EXTRAPOLACIÓN (CHART.JS)               -->
    <!-- ==================================================================== -->
    <section id="slide-11" class="slide-section py-4">
      <div class="space-y-4">
        <!-- Title -->
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-2 border-b border-slate-800 pb-3">
          <div>
            <div class="text-xs font-mono text-rose-400 uppercase tracking-wider">Laboratorio Empírico Chart.js</div>
            <h2 class="text-2xl md:text-3xl font-extrabold text-white">
              Demostración en Vivo: Regresión Lineal vs. Random Forest
            </h2>
          </div>
          <button onclick="regenerateExtrapolationData()" class="px-3 py-1 rounded bg-slate-800 hover:bg-slate-700 text-xs font-mono text-cyan-300 border border-slate-700 transition flex items-center gap-1">
            <i data-lucide="refresh-cw" class="w-3 h-3"></i>
            <span>Regenerar Ruido</span>
          </button>
        </div>

        <div class="glass-card p-5 rounded-2xl border border-slate-800 space-y-3">
          <div class="text-xs font-mono text-slate-300">
            Rango de Entrenamiento X &isin; [0, 7] vs Zona Oculta / Futuro X &isin; (7, 12]
          </div>

          <div class="relative w-full h-72 bg-slate-950 rounded-xl border border-slate-800 p-2">
            <canvas id="extrapolationChart"></canvas>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs font-mono pt-1">
            <div class="p-2.5 rounded-lg bg-cyan-950/30 border border-cyan-500/30 text-slate-300">
              <strong class="text-cyan-400">&bull; Regresión Lineal:</strong> Proyecta la pendiente continuamente hacia arriba en el futuro.
            </div>
            <div class="p-2.5 rounded-lg bg-rose-950/30 border border-rose-500/40 text-slate-300">
              <strong class="text-rose-400">&bull; Random Forest:</strong> Se aplana en una línea horizontal constante estancada en max(Y<sub>train</sub>).
            </div>
          </div>
        </div>

      </div>
    </section>

    <!-- ==================================================================== -->
    <!-- SLIDE 12: ARQUITECTURA: DEL NOTEBOOK A PRODUCCIÓN                    -->
    <!-- ==================================================================== -->
    <section id="slide-12" class="slide-section py-4">
      <div class="space-y-4">
        <!-- Title -->
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-2 border-b border-slate-800 pb-3">
          <div>
            <div class="text-xs font-mono text-cyan-400 uppercase tracking-wider">Ingeniería de Software & MLOps</div>
            <h2 class="text-2xl md:text-3xl font-extrabold text-white">
              Arquitectura: Del Notebook a Producción
            </h2>
          </div>
          <div class="text-xs font-mono text-cyan-300 bg-cyan-950 px-3 py-1.5 rounded border border-cyan-500/40">
            ONNX Runtime Desacoplado
          </div>
        </div>

        <!-- Horizontal Pipeline Diagram -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3">
          <!-- Step 1 -->
          <div class="glass-card p-4 rounded-xl border border-slate-800 space-y-2">
            <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-slate-800 text-slate-300">1. ENTRENAMIENTO</span>
            <h4 class="text-xs font-mono text-slate-200 font-bold">Notebook / Python</h4>
            <p class="text-[11px] text-slate-400 leading-snug">
              Scikit-Learn entrena los árboles offline. Selección de hiperparámetros y validación OOB.
            </p>
            <div class="text-[10px] font-mono text-cyan-400 bg-slate-950 p-1.5 rounded border border-slate-800">
              rf.fit(X_train, y_train)
            </div>
          </div>

          <!-- Step 2 -->
          <div class="glass-card p-4 rounded-xl border border-cyan-500/30 space-y-2">
            <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-cyan-950 text-cyan-300">2. DESACOPLAMIENTO</span>
            <h4 class="text-xs font-mono text-cyan-300 font-bold">Binario ONNX</h4>
            <p class="text-[11px] text-slate-400 leading-snug">
              Exportación del modelo a formato estándar <strong class="text-white">.onnx</strong> mediante <strong class="text-cyan-300">skl2onnx</strong>.
            </p>
            <div class="text-[10px] font-mono text-cyan-400 bg-slate-950 p-1.5 rounded border border-slate-800 truncate">
              to_onnx(rf, initial_types)
            </div>
          </div>

          <!-- Step 3 -->
          <div class="glass-card p-4 rounded-xl border border-emerald-500/30 space-y-2">
            <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-emerald-950 text-emerald-300">3. DESPLIEGUE</span>
            <h4 class="text-xs font-mono text-emerald-300 font-bold">Contenedor Docker</h4>
            <p class="text-[11px] text-slate-400 leading-snug">
              Imagen distroless ultraliviana (38 MB) sin intérprete de Python, pip ni librerías pesadas.
            </p>
            <div class="text-[10px] font-mono text-emerald-400 bg-slate-950 p-1.5 rounded border border-slate-800">
              FROM mcr.microsoft.com/dotnet
            </div>
          </div>

          <!-- Step 4 -->
          <div class="glass-card p-4 rounded-xl border border-amber-500/30 space-y-2">
            <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-amber-950 text-amber-300">4. EJECUCIÓN</span>
            <h4 class="text-xs font-mono text-amber-300 font-bold">Inferencia Nativa</h4>
            <p class="text-[11px] text-slate-400 leading-snug">
              Ejecución sobre C++ / C# / Go sin dependencia del intérprete de Python ni bloqueos por GIL.
            </p>
            <div class="text-[10px] font-mono text-amber-300 bg-slate-950 p-1.5 rounded border border-slate-800">
              Latencia P99: &lt; 1.5 ms
            </div>
          </div>
        </div>

        <!-- Detail Card -->
        <div class="glass-card p-4 rounded-xl border border-slate-800 text-xs text-slate-300 flex items-center justify-between">
          <div class="space-y-1">
            <span class="font-bold text-white font-mono">&bull; Desacoplamiento de Arquitectura:</span>
            <p class="text-slate-400 text-[11px]">
              Al eliminar Python de la ruta crítica de inferencia, se evitan fugas de memoria, se optimizan hilos nativos y se reducen costos de infraestructura cloud en un 80%.
            </p>
          </div>
          <button onclick="goToSlide(13)" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-cyan-300 font-mono text-xs flex items-center gap-1.5 transition ml-4">
            <span>Ver Paralelismo Hardware</span>
            <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
          </button>
        </div>

      </div>
    </section>

    <!-- ==================================================================== -->
    <!-- SLIDE 13: HARDWARE: PARALELISMO MASIVO EN CPU                        -->
    <!-- ==================================================================== -->
    <section id="slide-13" class="slide-section py-4">
      <div class="space-y-4">
        <!-- Title -->
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-2 border-b border-slate-800 pb-3">
          <div>
            <div class="text-xs font-mono text-amber-400 uppercase tracking-wider">Hardware & Concurrencia</div>
            <h2 class="text-2xl md:text-3xl font-extrabold text-white">
              Paralelismo de Hardware: Algoritmo Embarrassingly Parallel
            </h2>
          </div>
          <div class="text-xs font-mono text-amber-300 bg-amber-950 px-3 py-1.5 rounded border border-amber-500/40">
            Sin Locks de Memoria Compartida
          </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          
          <!-- Left: Simulation Visualizer -->
          <div class="lg:col-span-6 glass-card p-5 rounded-2xl border border-slate-800 space-y-3">
            <div class="flex items-center justify-between">
              <span class="text-xs font-mono text-slate-300 font-bold">100 Árboles Repartidos en Hilos de CPU</span>
              <button onclick="triggerCPULoadAnimation()" class="text-xs font-mono px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700">
                Lanzar Inferencia Paralela &rarr;
              </button>
            </div>

            <div class="grid grid-cols-2 gap-3" id="s13-cpu-cores-container">
              <div class="p-3 rounded-xl bg-slate-950 border border-slate-800">
                <div class="flex justify-between text-xs font-mono text-slate-400 mb-1">
                  <span>Hilo #0</span>
                  <span class="text-emerald-400 font-bold">25 árboles</span>
                </div>
                <div class="w-full h-2 bg-slate-800 rounded-full overflow-hidden">
                  <div class="h-full bg-emerald-400 w-0 core-bar transition-all duration-500"></div>
                </div>
              </div>
              <div class="p-3 rounded-xl bg-slate-950 border border-slate-800">
                <div class="flex justify-between text-xs font-mono text-slate-400 mb-1">
                  <span>Hilo #1</span>
                  <span class="text-emerald-400 font-bold">25 árboles</span>
                </div>
                <div class="w-full h-2 bg-slate-800 rounded-full overflow-hidden">
                  <div class="h-full bg-emerald-400 w-0 core-bar transition-all duration-500"></div>
                </div>
              </div>
              <div class="p-3 rounded-xl bg-slate-950 border border-slate-800">
                <div class="flex justify-between text-xs font-mono text-slate-400 mb-1">
                  <span>Hilo #2</span>
                  <span class="text-emerald-400 font-bold">25 árboles</span>
                </div>
                <div class="w-full h-2 bg-slate-800 rounded-full overflow-hidden">
                  <div class="h-full bg-emerald-400 w-0 core-bar transition-all duration-500"></div>
                </div>
              </div>
              <div class="p-3 rounded-xl bg-slate-950 border border-slate-800">
                <div class="flex justify-between text-xs font-mono text-slate-400 mb-1">
                  <span>Hilo #3</span>
                  <span class="text-emerald-400 font-bold">25 árboles</span>
                </div>
                <div class="w-full h-2 bg-slate-800 rounded-full overflow-hidden">
                  <div class="h-full bg-emerald-400 w-0 core-bar transition-all duration-500"></div>
                </div>
              </div>
            </div>

            <div class="text-[11px] font-mono text-slate-400 bg-slate-900/60 p-2.5 rounded-lg border border-slate-800">
              Reducción final por mayoría simple o promedio en &lt; 0.1 ms sin contención de memoria.
            </div>
          </div>

          <!-- Right: Exact Theory Bullets -->
          <div class="lg:col-span-6 glass-card p-5 rounded-2xl border border-slate-800 space-y-4">
            <h3 class="text-xs font-mono text-amber-400 uppercase tracking-wider font-bold flex items-center gap-2">
              <i data-lucide="cpu" class="w-4 h-4"></i>
              Fundamentos de Concurrencia
            </h3>

            <div class="space-y-3 text-xs text-slate-300 leading-relaxed">
              <p>
                <strong class="text-white block mb-1">&bull; Algoritmo embarrassingly parallel:</strong>
                Cada árbol de decisión es un clasificador independiente con su propia estructura en memoria. No existe intercambio de estado durante la inferencia.
              </p>

              <p>
                <strong class="text-white block mb-1">&bull; Inferencia distribuida en múltiples hilos:</strong>
                Se distribuye uniformemente en todos los núcleos de CPU disponibles sin bloqueos de sincronización mutua ni barreras de contención.
              </p>

              <div class="p-3 rounded-xl bg-slate-900 border border-slate-800 space-y-1">
                <span class="text-[10px] font-mono text-slate-400 uppercase block">&bull; Rendimiento Empírico:</span>
                <div class="flex justify-between text-xs font-mono">
                  <span class="text-slate-400">Throughput:</span>
                  <span class="text-emerald-400 font-bold">18,000 req/s por nodo</span>
                </div>
                <div class="flex justify-between text-xs font-mono">
                  <span class="text-slate-400">Latencia P99:</span>
                  <span class="text-cyan-400 font-bold">1.5 ms (28x vs Python)</span>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- ==================================================================== -->
    <!-- SLIDE 14: MATRIZ DE DECISIÓN TÉCNICA (2 COLUMNAS SIMÉTRICAS)         -->
    <!-- ==================================================================== -->
    <section id="slide-14" class="slide-section py-4">
      <div class="space-y-4">
        <!-- Title -->
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-2 border-b border-slate-800 pb-3">
          <div>
            <div class="text-xs font-mono text-emerald-400 uppercase tracking-wider">Criterio de Ingeniería en Producción</div>
            <h2 class="text-2xl md:text-3xl font-extrabold text-white">
              Matriz de Decisión Técnica
            </h2>
          </div>
          <div class="text-xs text-slate-400 font-mono bg-slate-900 px-3 py-1.5 rounded border border-slate-800">
            Cuándo SÍ vs. Cuándo DESCARTARLO
          </div>
        </div>

        <!-- Two Symmetric High-Contrast Columns -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 items-stretch">
          
          <!-- LEFT PANEL (GREEN): CUÁNDO SÍ -->
          <div class="glass-card p-6 rounded-2xl border border-emerald-500/40 bg-emerald-950/10 space-y-4 flex flex-col justify-between">
            <div class="space-y-3">
              <div class="flex items-center gap-2 border-b border-emerald-500/30 pb-3">
                <div class="w-7 h-7 rounded-lg bg-emerald-950 border border-emerald-500/40 flex items-center justify-center text-emerald-400">
                  <i data-lucide="check-circle-2" class="w-4 h-4"></i>
                </div>
                <h3 class="text-base font-bold font-mono text-emerald-400 uppercase tracking-wide">
                  Cuándo SÍ Seleccionarlo
                </h3>
              </div>

              <ul class="space-y-4 text-xs text-slate-200 leading-relaxed font-sans">
                <li class="flex items-start gap-2.5">
                  <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 mt-1.5 flex-shrink-0"></span>
                  <div>
                    <strong class="text-white block font-mono text-xs">Datos tabulares heterogéneos:</strong>
                    Excelente desempeño con relaciones fuertemente no lineales entre variables numéricas y categóricas.
                  </div>
                </li>

                <li class="flex items-start gap-2.5">
                  <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 mt-1.5 flex-shrink-0"></span>
                  <div>
                    <strong class="text-white block font-mono text-xs">Sin preprocesamiento de escala:</strong>
                    No requiere normalización, estandarización ni preprocesamiento complejo de escala o centrado de medias.
                  </div>
                </li>

                <li class="flex items-start gap-2.5">
                  <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 mt-1.5 flex-shrink-0"></span>
                  <div>
                    <strong class="text-white block font-mono text-xs">Alta tolerancia al sobreajuste:</strong>
                    Comportamiento muy robusto frente a hiperparámetros no óptimos; los árboles adicionales no sobreajustan.
                  </div>
                </li>
              </ul>
            </div>

            <div class="p-3 rounded-xl bg-emerald-950/40 border border-emerald-500/30 text-[11px] font-mono text-emerald-300">
              Veredicto: Benchmark estándar y baseline mandatorio en proyectos tabulares.
            </div>
          </div>

          <!-- RIGHT PANEL (RED): CUÁNDO DESCARTARLO -->
          <div class="glass-card p-6 rounded-2xl border border-rose-500/40 bg-rose-950/10 space-y-4 flex flex-col justify-between">
            <div class="space-y-3">
              <div class="flex items-center gap-2 border-b border-rose-500/30 pb-3">
                <div class="w-7 h-7 rounded-lg bg-rose-950 border border-rose-500/40 flex items-center justify-center text-rose-400">
                  <i data-lucide="x-circle" class="w-4 h-4"></i>
                </div>
                <h3 class="text-base font-bold font-mono text-rose-400 uppercase tracking-wide">
                  Cuándo DESCARTARLO
                </h3>
              </div>

              <ul class="space-y-4 text-xs text-slate-200 leading-relaxed font-sans">
                <li class="flex items-start gap-2.5">
                  <span class="w-1.5 h-1.5 rounded-full bg-rose-400 mt-1.5 flex-shrink-0"></span>
                  <div>
                    <strong class="text-white block font-mono text-xs">Series temporales con tendencia:</strong>
                    Proyecciones con tendencia alcista/bajista fallan por el límite de extrapolación matemática ortogonal.
                  </div>
                </li>

                <li class="flex items-start gap-2.5">
                  <span class="w-1.5 h-1.5 rounded-full bg-rose-400 mt-1.5 flex-shrink-0"></span>
                  <div>
                    <strong class="text-white block font-mono text-xs">Restricciones críticas de memoria RAM:</strong>
                    Entornos embebidos o microcontroladores IoT con &lt; 2 MB RAM sufren con el peso de los árboles.
                  </div>
                </li>

                <li class="flex items-start gap-2.5">
                  <span class="w-1.5 h-1.5 rounded-full bg-rose-400 mt-1.5 flex-shrink-0"></span>
                  <div>
                    <strong class="text-white block font-mono text-xs">Latencia ultraestricta sub-milisegundo:</strong>
                    Sistemas que demanden respuestas en microsegundos (HFT o edge computing ligero) donde modelos lineales o tablas dominan.
                  </div>
                </li>
              </ul>
            </div>

            <div class="p-3 rounded-xl bg-rose-950/40 border border-rose-500/30 text-[11px] font-mono text-rose-300">
              Veredicto: Descartar ante series con tendencia, RAM extrema o texto libre NLP.
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- ==================================================================== -->
    <!-- SLIDE 15: ASISTENTE INTERACTIVO DE DECISIÓN (QUIZ) Y CIERRE          -->
    <!-- ==================================================================== -->
    <section id="slide-15" class="slide-section py-4">
      <div class="space-y-4">
        <!-- Title -->
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-2 border-b border-slate-800 pb-3">
          <div>
            <div class="text-xs font-mono text-cyan-400 uppercase tracking-wider">Cierre & Diagnóstico</div>
            <h2 class="text-2xl md:text-3xl font-extrabold text-white">
              Asistente Interactivo de Decisión Técnica
            </h2>
          </div>
          <button onclick="goToSlide(1)" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-mono text-slate-200 border border-slate-700 transition">
            Volver a Portada
          </button>
        </div>

        <!-- 3 Questions Quiz -->
        <div class="glass-card p-5 rounded-2xl border border-slate-800 space-y-4">
          <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2">
              <label class="text-xs font-mono text-slate-300 block">1. &iquest;Naturaleza de los datos?</label>
              <select id="quiz-q1" onchange="runQuizEvaluation()" class="w-full text-xs font-mono bg-slate-950 border border-slate-700 text-slate-200 rounded p-2">
                <option value="tabular">Tabulares (Clientes, Sensores, Finanzas)</option>
                <option value="text">Texto no estructurado / NLP</option>
                <option value="image">Imágenes / Audio continuo</option>
              </select>
            </div>

            <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2">
              <label class="text-xs font-mono text-slate-300 block">2. &iquest;Tendencia temporal con extrapolación?</label>
              <select id="quiz-q2" onchange="runQuizEvaluation()" class="w-full text-xs font-mono bg-slate-950 border border-slate-700 text-slate-200 rounded p-2">
                <option value="no">No (Clasificación o predicción estática)</option>
                <option value="yes">Sí (Serie temporal con crecimiento sostenido)</option>
              </select>
            </div>

            <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2">
              <label class="text-xs font-mono text-slate-300 block">3. &iquest;Restricciones extremas de memoria RAM?</label>
              <select id="quiz-q3" onchange="runQuizEvaluation()" class="w-full text-xs font-mono bg-slate-950 border border-slate-700 text-slate-200 rounded p-2">
                <option value="server">Servidor Cloud / Máquina estándar (RAM holgada)</option>
                <option value="edge">Dispositivo Edge / Microcontrolador (&lt; 2MB RAM)</option>
              </select>
            </div>
          </div>

          <!-- Dynamic Verdict Box -->
          <div id="quiz-result-box" class="p-4 rounded-xl bg-emerald-950/40 border border-emerald-500/40 flex items-center justify-between">
            <div>
              <span class="text-[10px] font-mono text-slate-400 uppercase block">Veredicto Recomendado:</span>
              <div id="quiz-verdict-title" class="text-base font-bold font-mono text-emerald-400">
                &check; RANDOM FOREST ES TU ELECCIÓN ÓPTIMA
              </div>
              <p id="quiz-verdict-desc" class="text-xs text-slate-300 mt-0.5">
                Datos tabulares estándar sin tendencia de extrapolación. Aprovecharás su robustez y paralelismo natural.
              </p>
            </div>
            <div class="w-8 h-8 rounded-full bg-emerald-950 border border-emerald-500/50 flex items-center justify-center text-emerald-400 flex-shrink-0">
              <i data-lucide="check" class="w-5 h-5"></i>
            </div>
          </div>

          <!-- Takeaway Credits -->
          <div class="pt-2 border-t border-slate-800 flex flex-col sm:flex-row items-center justify-between text-xs font-mono text-slate-400 gap-2">
            <span>Presentación elaborada por <strong>Denshel David Mérida Quispe</strong></span>
            <span class="text-cyan-400">Leo Breiman (2001) &bull; Condorcet (1785) &bull; Lundberg & Lee (2017)</span>
          </div>
        </div>

      </div>
    </section>

  </main>

  <!-- ==================================================================== -->
  <!-- FIXED BOTTOM NAVIGATION BAR                                          -->
  <!-- ==================================================================== -->
  <footer class="w-full fixed bottom-0 left-0 z-50 bg-slate-950/95 backdrop-blur-md border-t border-slate-800/80 px-4 md:px-8 py-3">
    <div class="max-w-7xl mx-auto flex items-center justify-between">
      
      <!-- Left: Previous Button & Slide Counter -->
      <div class="flex items-center gap-3">
        <button id="btn-prev" onclick="prevSlide()" class="px-3.5 py-1.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-700/60 text-slate-300 hover:text-white transition flex items-center gap-2 text-xs font-mono">
          <i data-lucide="chevron-left" class="w-4 h-4"></i>
          <span class="hidden sm:inline">Anterior</span>
          <kbd class="px-1.5 py-0.5 text-[10px] bg-slate-800 border border-slate-700 rounded text-slate-400">&larr;</kbd>
        </button>

        <div class="text-xs font-mono text-slate-400 hidden sm:block">
          Diapositiva <span id="nav-current-slide" class="text-emerald-400 font-bold">1</span> de <span id="nav-total-slides">15</span>
        </div>
      </div>

      <!-- Center: 15 Dot Navigation Menu -->
      <nav id="dots-container" class="flex items-center gap-1 sm:gap-1.5" aria-label="Selector rápido de diapositiva">
        <!-- Injected via JS -->
      </nav>

      <!-- Right: Next Button -->
      <div class="flex items-center gap-2">
        <button id="btn-next" onclick="nextSlide()" class="px-3.5 py-1.5 rounded-xl bg-gradient-to-r from-emerald-500 to-teal-600 hover:from-emerald-400 text-slate-950 font-bold transition flex items-center gap-2 text-xs font-mono shadow-md shadow-emerald-500/20">
          <span class="hidden sm:inline">Siguiente</span>
          <kbd class="px-1.5 py-0.5 text-[10px] bg-slate-950/30 border border-slate-950/40 rounded text-slate-900 font-sans">&rarr;</kbd>
          <i data-lucide="chevron-right" class="w-4 h-4"></i>
        </button>
      </div>

    </div>
  </footer>

  <!-- ==================================================================== -->
  <!-- KEYBOARD SHORTCUTS HELP MODAL                                        -->
  <!-- ==================================================================== -->
  <div id="shortcuts-modal" class="fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-md hidden items-center justify-center p-4">
    <div class="glass-card max-w-md w-full p-6 rounded-2xl border border-slate-800 shadow-2xl space-y-4">
      <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2 text-cyan-400 font-mono font-bold text-sm">
          <i data-lucide="keyboard" class="w-5 h-5"></i>
          Atajos de Teclado del Presentador
        </div>
        <button onclick="toggleHelpModal()" class="text-slate-400 hover:text-white p-1 rounded">
          <i data-lucide="x" class="w-5 h-5"></i>
        </button>
      </div>

      <div class="text-xs font-mono text-slate-300 space-y-2.5">
        <div class="flex justify-between items-center py-1 border-b border-slate-800/60">
          <span>Siguiente Diapositiva:</span>
          <span class="text-cyan-400">&rarr; / Espacio / Enter</span>
        </div>
        <div class="flex justify-between items-center py-1 border-b border-slate-800/60">
          <span>Diapositiva Anterior:</span>
          <span class="text-cyan-400">&larr; / Backspace</span>
        </div>
        <div class="flex justify-between items-center py-1 border-b border-slate-800/60">
          <span>Alternar Pantalla Completa:</span>
          <span class="text-cyan-400">Tecla F</span>
        </div>
        <div class="flex justify-between items-center py-1 border-b border-slate-800/60">
          <span>Abrir / Cerrar Ayuda:</span>
          <span class="text-cyan-400">Tecla ? o Esc</span>
        </div>
      </div>

      <div class="text-right">
        <button onclick="toggleHelpModal()" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-mono text-slate-200">
          Cerrar
        </button>
      </div>
    </div>
  </div>

  <!-- ==================================================================== -->
  <!-- JAVASCRIPT APPLICATION CORE LOGIC                                    -->
  <!-- ==================================================================== -->
  <script>
    /* ---------------------------------------------------------------------- */
    /* 1. GLOBAL STATE & NAVIGATION ENGINE (15 SLIDES)                        */
    /* ---------------------------------------------------------------------- */
    let currentSlide = 1;
    const totalSlides = 15;
    let isAnimating = false;

    const slideTopics = [
      "1. Portada",
      "2. Teorema de Condorcet",
      "3. Caso de Estudio: Señales",
      "4. Bagging (Muestreo con Reemplazo)",
      "5. Subespacio Aleatorio",
      "6. Reducción de Varianza",
      "7. Matriz de Predicciones",
      "8. Auditoría XAI (SHAP vs Gini)",
      "9. SHAP Beeswarm Plot",
      "10. Límite de Extrapolación",
      "11. Experimento en Vivo (Chart.js)",
      "12. Arquitectura ONNX",
      "13. Hardware y Paralelismo CPU",
      "14. Matriz de Decisión Técnica",
      "15. Asistente y Cierre"
    ];

    function initDots() {
      const container = document.getElementById('dots-container');
      container.innerHTML = '';
      for (let i = 1; i <= totalSlides; i++) {
        const dot = document.createElement('button');
        dot.className = i === 1 
          ? 'slide-dot w-2 h-2 sm:w-2.5 sm:h-2.5 rounded-full bg-emerald-400 ring-4 ring-emerald-500/20 transition-all'
          : 'slide-dot w-2 h-2 sm:w-2.5 sm:h-2.5 rounded-full bg-slate-700 hover:bg-slate-500 transition-all';
        dot.title = slideTopics[i - 1];
        dot.onclick = () => goToSlide(i);
        container.appendChild(dot);
      }
    }

    function updateNavigationUI() {
      document.getElementById('header-counter-current').textContent = currentSlide;
      document.getElementById('header-counter-total').textContent = totalSlides;
      document.getElementById('nav-current-slide').textContent = currentSlide;
      document.getElementById('nav-total-slides').textContent = totalSlides;
      document.getElementById('header-slide-topic').textContent = slideTopics[currentSlide - 1];

      // Progress bar fill with GSAP
      const progressPercent = (currentSlide / totalSlides) * 100;
      gsap.to('#progress-bar-fill', {
        width: `${progressPercent}%`,
        duration: 0.35,
        ease: 'power2.out'
      });

      // Update dots
      const dots = document.querySelectorAll('.slide-dot');
      dots.forEach((dot, idx) => {
        if (idx === currentSlide - 1) {
          dot.className = 'slide-dot w-2 h-2 sm:w-2.5 sm:h-2.5 rounded-full bg-emerald-400 ring-4 ring-emerald-500/30 transition-all';
        } else {
          dot.className = 'slide-dot w-2 h-2 sm:w-2.5 sm:h-2.5 rounded-full bg-slate-700 hover:bg-slate-500 transition-all';
        }
      });
    }

    function goToSlide(targetSlide) {
      if (targetSlide < 1 || targetSlide > totalSlides || targetSlide === currentSlide || isAnimating) return;
      isAnimating = true;

      const currentElem = document.getElementById('slide-' + currentSlide);
      const targetElem = document.getElementById('slide-' + targetSlide);

      const direction = targetSlide > currentSlide ? 1 : -1;

      const tl = gsap.timeline({
        onComplete: () => {
          currentElem.classList.remove('active');
          currentElem.style.display = 'none';
          targetElem.classList.add('active');
          targetElem.style.display = 'block';
          currentSlide = targetSlide;
          updateNavigationUI();
          isAnimating = false;
          onSlideEnter(currentSlide);
        }
      });

      tl.to(currentElem, {
        opacity: 0,
        x: -40 * direction,
        duration: 0.25,
        ease: 'power2.in'
      });

      targetElem.style.display = 'block';
      gsap.set(targetElem, { opacity: 0, x: 40 * direction });

      tl.to(targetElem, {
        opacity: 1,
        x: 0,
        duration: 0.35,
        ease: 'power2.out'
      });

      tl.from(targetElem.querySelectorAll('.glass-card, h2, .grid > div'), {
        opacity: 0,
        y: 12,
        duration: 0.3,
        stagger: 0.04,
        ease: 'power2.out'
      }, "-=0.2");
    }

    function nextSlide() {
      if (currentSlide < totalSlides) {
        goToSlide(currentSlide + 1);
      }
    }

    function prevSlide() {
      if (currentSlide > 1) {
        goToSlide(currentSlide - 1);
      }
    }

    function onSlideEnter(slideNum) {
      if (slideNum === 2) {
        updateCondorcetSimulator();
      } else if (slideNum === 3) {
        renderRoadSign();
        updateSignClassifiers();
      } else if (slideNum === 4) {
        initSlide4();
      } else if (slideNum === 5) {
        renderSubspaceFeatures();
      } else if (slideNum === 6) {
        updateVarianceSimulator();
      } else if (slideNum === 7) {
        initSlide7MLUMatrix();
      } else if (slideNum === 9) {
        initSlide9ShapPlot();
      } else if (slideNum === 11) {
        initSlide11ExtrapolationChart();
      } else if (slideNum === 13) {
        triggerCPULoadAnimation();
      }
      lucide.createIcons();
    }

    /* ---------------------------------------------------------------------- */
    /* 2. KEYBOARD NAVIGATION & SHORTCUTS                                     */
    /* ---------------------------------------------------------------------- */
    window.addEventListener('keydown', (e) => {
      if (['INPUT', 'SELECT', 'TEXTAREA'].includes(e.target.tagName)) return;

      if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'Enter') {
        e.preventDefault();
        nextSlide();
      } else if (e.key === 'ArrowLeft' || e.key === 'Backspace') {
        e.preventDefault();
        prevSlide();
      } else if (e.key.toLowerCase() === 'f') {
        toggleFullScreen();
      } else if (e.key === '?' || (e.shiftKey && e.key === '/')) {
        toggleHelpModal();
      } else if (e.key === 'Escape') {
        closeAllModals();
      }
    });

    function toggleFullScreen() {
      if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(() => {});
      } else {
        if (document.exitFullscreen) document.exitFullscreen();
      }
    }

    function toggleHelpModal() {
      const modal = document.getElementById('shortcuts-modal');
      modal.classList.toggle('hidden');
      modal.classList.toggle('flex');
    }

    function closeAllModals() {
      document.getElementById('shortcuts-modal').classList.add('hidden');
      document.getElementById('shortcuts-modal').classList.remove('flex');
    }

    document.getElementById('btn-fullscreen').addEventListener('click', toggleFullScreen);
    document.getElementById('btn-help').addEventListener('click', toggleHelpModal);


    /* ---------------------------------------------------------------------- */
    /* 3. SLIDE 2: CONDORCET JURY THEOREM SIMULATOR                           */
    /* ---------------------------------------------------------------------- */
    function combination(n, k) {
      if (k < 0 || k > n) return 0;
      if (k === 0 || k === n) return 1;
      let c = 1;
      for (let i = 1; i <= k; i++) {
        c = (c * (n - (k - i))) / i;
      }
      return c;
    }

    function calcCondorcetProb(p, n) {
      const kMin = Math.ceil(n / 2);
      let sum = 0;
      for (let k = kMin; k <= n; k++) {
        sum += combination(n, k) * Math.pow(p, k) * Math.pow(1 - p, n - k);
      }
      return sum;
    }

    function updateCondorcetSimulator() {
      const pSlider = document.getElementById('condorcet-p-slider');
      const nSlider = document.getElementById('condorcet-n-slider');
      const isCorrelated = document.getElementById('condorcet-corr-toggle').checked;

      const p = parseFloat(pSlider.value);
      const n = parseInt(nSlider.value);

      document.getElementById('condorcet-p-val').textContent = (p * 100).toFixed(1) + '%';
      document.getElementById('condorcet-n-val').textContent = `${n} árboles`;

      let finalProb = calcCondorcetProb(p, n);
      if (isCorrelated) {
        finalProb = p;
      }

      const percent = (finalProb * 100).toFixed(1);
      const metricElem = document.getElementById('condorcet-result-metric');
      const subtextElem = document.getElementById('condorcet-subtext');

      metricElem.textContent = `${percent}%`;
      const majorityK = Math.ceil(n / 2);
      document.getElementById('condorcet-majority-req').textContent = `≥ ${majorityK} de ${n} votos`;

      if (isCorrelated) {
        metricElem.className = 'text-4xl sm:text-5xl font-black text-rose-400 tracking-tight font-mono';
        subtextElem.innerHTML = `<span class="text-rose-400 font-bold">Sin ganancia de ensamble:</span> Correlación = 1.0 (los modelos repiten idéntico error).`;
      } else {
        metricElem.className = 'text-4xl sm:text-5xl font-black text-emerald-400 tracking-tight font-mono text-glow-emerald';
        const gain = (finalProb * 100 - p * 100).toFixed(1);
        subtextElem.innerHTML = `Supera en <span class="text-cyan-300 font-bold">+${gain}%</span> la precisión de cualquier árbol individual`;
      }

      const container = document.getElementById('condorcet-trees-container');
      container.innerHTML = '';
      
      const expectedCorrect = Math.round(n * (isCorrelated ? p : finalProb));
      for (let i = 0; i < n; i++) {
        const isCorrect = i < expectedCorrect;
        const treeDiv = document.createElement('div');
        treeDiv.className = `p-1 rounded-lg flex flex-col items-center justify-center border text-[9px] font-mono transition-all ${
          isCorrect 
            ? 'bg-emerald-950/60 border-emerald-500/40 text-emerald-300' 
            : 'bg-rose-950/60 border-rose-500/40 text-rose-300'
        }`;
        treeDiv.innerHTML = `
          <svg class="w-4 h-4 mb-0.5" viewBox="0 0 24 24" fill="${isCorrect ? 'rgba(52,211,153,0.3)' : 'rgba(251,113,133,0.3)'}" stroke="currentColor" stroke-width="1.5">
            <polygon points="12 2 5 12 9 12 7 18 17 18 15 12 19 12 12 2"/>
            <rect x="11" y="18" width="2" height="4" fill="#047857"/>
          </svg>
          <span>T<sub>${i + 1}</sub>:${isCorrect ? '✓' : '✗'}</span>
        `;
        container.appendChild(treeDiv);
      }
    }

    document.getElementById('condorcet-p-slider').addEventListener('input', updateCondorcetSimulator);
    document.getElementById('condorcet-n-slider').addEventListener('input', updateCondorcetSimulator);
    document.getElementById('condorcet-corr-toggle').addEventListener('change', updateCondorcetSimulator);


    /* ---------------------------------------------------------------------- */
    /* 4. SLIDE 3: CASO DE ESTUDIO (SEÑALES VIALES)                           */
    /* ---------------------------------------------------------------------- */
    function onSignSelectorChange() {
      renderRoadSign();
      updateSignClassifiers();
    }

    function loadSignEdgeCase() {
      document.getElementById('feat-size').value = 'Mediano';
      document.getElementById('feat-shape').value = 'Círculo (1)';
      document.getElementById('feat-color').value = 'Bicolor';
      document.getElementById('feat-content').value = 'Persona';
      renderRoadSign();
      updateSignClassifiers();
    }

    function renderRoadSign() {
      const size = document.getElementById('feat-size').value;
      const shape = document.getElementById('feat-shape').value;
      const color = document.getElementById('feat-color').value;
      const content = document.getElementById('feat-content').value;

      document.getElementById('sign-summary-text').textContent = `${size} • ${shape} • ${color} • ${content}`;

      const wrapper = document.getElementById('sign-svg-wrapper');
      let shapeSvg = '';

      let fillColor = '#0284c7';
      let strokeColor = '#ffffff';

      if (color === 'Monocromo') fillColor = '#334155';
      else if (color === 'Multicolor') fillColor = '#dc2626';

      if (shape.includes('Triángulo')) {
        shapeSvg = `<polygon points="32,6 6,56 58,56" fill="${fillColor}" stroke="${strokeColor}" stroke-width="2.5"/>`;
      } else if (shape.includes('Rombo')) {
        shapeSvg = `<polygon points="32,6 58,32 32,58 6,32" fill="${fillColor}" stroke="${strokeColor}" stroke-width="2.5"/>`;
      } else if (shape.includes('Octágono')) {
        shapeSvg = `<polygon points="20,6 44,6 58,20 58,44 44,58 20,58 6,44 6,20" fill="${fillColor}" stroke="${strokeColor}" stroke-width="2.5"/>`;
      } else {
        shapeSvg = `<circle cx="32" cy="32" r="26" fill="${fillColor}" stroke="${strokeColor}" stroke-width="2.5"/>`;
      }

      let contentSvg = '';
      if (content === 'Persona') {
        contentSvg = `
          <circle cx="32" cy="22" r="3.5" fill="#ffffff"/>
          <path d="M28,32 L36,32 L34,44 L30,44 Z" fill="#ffffff"/>
          <line x1="28" y1="28" x2="23" y2="36" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
          <line x1="36" y1="28" x2="41" y2="34" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
          <line x1="30" y1="44" x2="26" y2="52" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round"/>
          <line x1="34" y1="44" x2="38" y2="52" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round"/>
        `;
      } else {
        contentSvg = `
          <text x="32" y="37" font-size="10" font-family="sans-serif" font-weight="900" fill="#ffffff" text-anchor="middle">STOP</text>
        `;
      }

      wrapper.innerHTML = `
        <svg class="w-16 h-16 drop-shadow-lg" viewBox="0 0 64 64">
          ${shapeSvg}
          ${contentSvg}
        </svg>
      `;
    }

    function updateSignClassifiers() {
      const shape = document.getElementById('feat-shape').value;
      const color = document.getElementById('feat-color').value;
      const content = document.getElementById('feat-content').value;
      const size = document.getElementById('feat-size').value;

      const isTriangle = shape.includes('Triángulo');
      const isBicolor = color === 'Bicolor';
      const hasPerson = content === 'Persona';

      // 1. Single Decision Tree
      const singlePredictsYes = isTriangle && isBicolor && hasPerson;
      const singleElem = document.getElementById('single-tree-verdict');
      if (singlePredictsYes) {
        singleElem.className = 'text-xs font-mono font-bold px-2 py-1 rounded bg-emerald-950 text-emerald-400 border border-emerald-500/40';
        singleElem.textContent = 'SÍ (CRUCE)';
      } else {
        singleElem.className = 'text-xs font-mono font-bold px-2 py-1 rounded bg-rose-950 text-rose-400 border border-rose-500/40';
        singleElem.textContent = 'NO CRUCE (FALLO)';
      }

      // 2. Random Forest (5 Trees)
      const t1 = (isTriangle || shape.includes('Círculo')) && hasPerson;
      const t2 = hasPerson;
      const t3 = (isBicolor || color === 'Multicolor') && hasPerson;
      const t4 = isTriangle;
      const t5 = (size !== 'Pequeño') && hasPerson;

      const votes = [t1, t2, t3, t4, t5];
      const yesVotes = votes.filter(Boolean).length;
      const isConsensusYes = yesVotes >= 3;

      const forestElem = document.getElementById('forest-verdict');
      if (isConsensusYes) {
        forestElem.className = 'text-xs font-mono font-bold px-2 py-1 rounded bg-emerald-950 text-emerald-400 border border-emerald-500/40';
        forestElem.textContent = `SÍ (${yesVotes}/5 Votos - ${(yesVotes/5*100).toFixed(0)}%)`;
      } else {
        forestElem.className = 'text-xs font-mono font-bold px-2 py-1 rounded bg-rose-950 text-rose-400 border border-rose-500/40';
        forestElem.textContent = `NO (${5 - yesVotes}/5 Votos)`;
      }
    }


    /* ---------------------------------------------------------------------- */
    /* 5. SLIDE 4: BAGGING SIMULATION                                         */
    /* ---------------------------------------------------------------------- */
    const sampleDataset = [
      { id: 'D₁', text: 'Señal 1 (Peatón, Azul)' },
      { id: 'D₂', text: 'Señal 2 (STOP, Octágono)' },
      { id: 'D₃', text: 'Señal 3 (Ceda, Triángulo)' },
      { id: 'D₄', text: 'Señal 4 (Peatón, Rombo)' },
      { id: 'D₅', text: 'Señal 5 (Velocidad, Círculo)' },
      { id: 'D₆', text: 'Señal 6 (Peatón, Triángulo)' },
      { id: 'D₇', text: 'Señal 7 (Curva Peligrosa)' },
      { id: 'D₈', text: 'Señal 8 (Peatón, Monocromo)' },
      { id: 'D₉', text: 'Señal 9 (Prohibido Girar)' },
      { id: 'D₁₀', text: 'Señal 10 (Obras Calzada)' }
    ];

    function initSlide4() {
      const orig = document.getElementById('s4-original-list');
      orig.innerHTML = sampleDataset.map(d => `
        <div class="px-2 py-1 rounded bg-slate-900 border border-slate-800 flex justify-between items-center text-[11px] font-mono">
          <span class="text-cyan-400 font-bold">${d.id}</span>
          <span class="text-slate-300 truncate">${d.text}</span>
        </div>
      `).join('');
      generateBootstrapSample();
    }

    function generateBootstrapSample() {
      const n = sampleDataset.length;
      const counts = {};

      for (let i = 0; i < n; i++) {
        const randIdx = Math.floor(Math.random() * n);
        counts[randIdx] = (counts[randIdx] || 0) + 1;
      }

      const bootstrapContainer = document.getElementById('s4-bootstrap-list');
      bootstrapContainer.innerHTML = '';

      let uniqueCount = 0;
      let oobCount = 0;

      sampleDataset.forEach((item, idx) => {
        const count = counts[idx] || 0;
        const row = document.createElement('div');
        if (count > 0) {
          uniqueCount++;
          row.className = 'px-2 py-1 rounded bg-emerald-950/60 border border-emerald-500/40 flex justify-between items-center text-[11px] font-mono text-emerald-300';
          row.innerHTML = `
            <span>${item.id} (${item.text.split(' ')[1]})</span>
            <span class="px-1.5 py-0.2 rounded bg-emerald-900 border border-emerald-400 text-[10px] font-bold">x${count}</span>
          `;
        } else {
          oobCount++;
          row.className = 'px-2 py-1 rounded bg-slate-950 border border-slate-800 flex justify-between items-center text-[11px] font-mono text-slate-500';
          row.innerHTML = `
            <span>${item.id} (Fuera)</span>
            <span class="text-[10px] text-rose-400 font-bold">OOB</span>
          `;
        }
        bootstrapContainer.appendChild(row);
      });

      document.getElementById('s4-inbag-count').textContent = `${uniqueCount} únicas (${n} con reemplazo)`;
      document.getElementById('s4-oob-count').textContent = `${oobCount} muestras OOB (${(oobCount / n * 100).toFixed(0)}%)`;

      gsap.from('#s4-bootstrap-list > div', {
        scale: 0.95,
        opacity: 0,
        stagger: 0.02,
        duration: 0.2
      });
    }


    /* ---------------------------------------------------------------------- */
    /* 6. SLIDE 5: RANDOM SUBSPACE SIMULATION                                 */
    /* ---------------------------------------------------------------------- */
    const allFeatures = ['1. Tamaño', '2. Número de Caras', '3. Colores', '4. Texto o Símbolo'];
    let activeSubset = [0, 2];

    function renderSubspaceFeatures() {
      const container = document.getElementById('s5-features-subspace-container');
      container.innerHTML = allFeatures.map((f, idx) => {
        const isSelected = activeSubset.includes(idx);
        return `
          <div class="p-3 rounded-xl border flex flex-col items-center justify-center transition-all ${
            isSelected 
              ? 'bg-cyan-950/70 border-cyan-400 text-cyan-300 shadow-lg shadow-cyan-500/10' 
              : 'bg-slate-950/80 border-slate-800 text-slate-600 opacity-50'
          }">
            <div class="mb-1">${isSelected ? '🔓' : '🔒'}</div>
            <span class="text-xs font-mono font-bold text-center">${f}</span>
            <span class="text-[9px] font-mono mt-1 ${isSelected ? 'text-cyan-400' : 'text-slate-500'}">
              ${isSelected ? 'Disponible en Nodo' : 'Oculta aleatoriamente'}
            </span>
          </div>
        `;
      }).join('');

      const activeNames = activeSubset.map(idx => allFeatures[idx]).join(' y ');
      document.getElementById('s5-active-split-badge').textContent = `Buscando división óptima entre: ${activeNames}`;
    }

    function simulateNodeSplit() {
      const indices = [0, 1, 2, 3];
      for (let i = indices.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [indices[i], indices[j]] = [indices[j], indices[i]];
      }
      activeSubset = indices.slice(0, 2);
      renderSubspaceFeatures();

      gsap.from('#s5-features-subspace-container > div', {
        scale: 0.9,
        duration: 0.25,
        stagger: 0.04
      });
    }


    /* ---------------------------------------------------------------------- */
    /* 7. SLIDE 6: VARIANCE REDUCTION CALCULATOR                              */
    /* ---------------------------------------------------------------------- */
    function updateVarianceSimulator() {
      const rho = parseFloat(document.getElementById('var-rho-slider').value);
      const b = parseInt(document.getElementById('var-b-slider').value);

      document.getElementById('var-rho-val').textContent = rho.toFixed(2);
      document.getElementById('var-b-val').textContent = `${b} árboles`;

      const irreducible = rho;
      const reducible = (1 - rho) / b;
      const total = irreducible + reducible;

      document.getElementById('var-total-val').textContent = `${total.toFixed(3)} \u03C3\u00B2`;
      document.getElementById('var-irred-val').textContent = `${irreducible.toFixed(2)} \u03C3\u00B2`;
      document.getElementById('var-red-val').textContent = `${reducible.toFixed(3)} \u03C3\u00B2`;

      const irredPercent = (irreducible / 1.0) * 100;
      const redPercent = (reducible / 1.0) * 100;

      document.getElementById('var-bar-irreducible').style.width = `${irredPercent}%`;
      document.getElementById('var-bar-reducible').style.width = `${redPercent}%`;
    }

    document.getElementById('var-rho-slider').addEventListener('input', updateVarianceSimulator);
    document.getElementById('var-b-slider').addEventListener('input', updateVarianceSimulator);


    /* ---------------------------------------------------------------------- */
    /* 8. SLIDE 7: PREDICTION MATRIX (9 x 6)                                  */
    /* ---------------------------------------------------------------------- */
    const initialMatrix = [
      [true,  true,  false, true,  true,  true ],
      [false, true,  true,  true,  false, true ],
      [true,  false, true,  true,  true,  true ],
      [true,  true,  true,  false, true,  true ],
      [true,  true,  true,  true,  true,  false],
      [false, true,  true,  true,  true,  true ],
      [true,  false, true,  true,  true,  true ],
      [true,  true,  false, true,  true,  true ],
      [true,  true,  true,  true,  false, true ]
    ];

    let currentMatrix = JSON.parse(JSON.stringify(initialMatrix));

    function initSlide7MLUMatrix() {
      renderMLUMatrix();
    }

    function toggleMatrixCell(row, col) {
      currentMatrix[row][col] = !currentMatrix[row][col];
      renderMLUMatrix();
    }

    function resetMLUMatrix() {
      currentMatrix = JSON.parse(JSON.stringify(initialMatrix));
      renderMLUMatrix();
    }

    function renderMLUMatrix() {
      const tbody = document.getElementById('mlu-matrix-body');
      tbody.innerHTML = '';

      const colVotes = [0, 0, 0, 0, 0, 0];

      currentMatrix.forEach((treeRow, rIdx) => {
        let correctCount = 0;
        const tr = document.createElement('tr');
        tr.className = 'hover:bg-slate-900/40 transition';

        let cellsHtml = `<td class="py-2 px-3 text-left font-bold text-slate-300">Árbol ${rIdx + 1}</td>`;

        treeRow.forEach((isCorrect, cIdx) => {
          if (isCorrect) {
            correctCount++;
            colVotes[cIdx]++;
          }
          cellsHtml += `
            <td class="py-1.5 px-2 cursor-pointer" onclick="toggleMatrixCell(${rIdx}, ${cIdx})" title="Haz clic para alternar acierto/error">
              <span class="inline-flex items-center justify-center w-6 h-6 rounded-full text-xs font-bold transition-transform hover:scale-125 ${
                isCorrect 
                  ? 'bg-emerald-950 text-emerald-400 border border-emerald-500/50' 
                  : 'bg-striped-rose text-rose-300 border border-rose-500/50 font-bold'
              }">
                ${isCorrect ? '✓' : '✗'}
              </span>
            </td>
          `;
        });

        const accuracy = (correctCount / 6 * 100).toFixed(0);
        cellsHtml += `<td class="py-2 px-3 text-right font-mono ${accuracy >= 80 ? 'text-emerald-400' : 'text-slate-400'}">${accuracy}%</td>`;

        tr.innerHTML = cellsHtml;
        tbody.appendChild(tr);
      });

      const tfoot = document.getElementById('mlu-matrix-foot');
      let footHtml = `
        <tr class="font-bold">
          <td class="py-2.5 px-3 text-left text-emerald-300 font-mono flex items-center gap-1.5">
            <i data-lucide="award" class="w-4 h-4 text-emerald-400"></i>
            VOTO MAYORITARIO (BOSQUE)
          </td>
      `;

      let ensembleCorrectCount = 0;
      colVotes.forEach((votes) => {
        const isConsensusCorrect = votes >= 5;
        if (isConsensusCorrect) ensembleCorrectCount++;
        footHtml += `
          <td class="py-2 px-2">
            <div class="flex flex-col items-center">
              <span class="w-6 h-6 rounded-full flex items-center justify-center font-bold text-xs ${
                isConsensusCorrect 
                  ? 'bg-emerald-500 text-slate-950 shadow-md shadow-emerald-500/30' 
                  : 'bg-rose-500 text-white shadow-md shadow-rose-500/30'
              }">
                ${isConsensusCorrect ? '✓' : '✗'}
              </span>
              <span class="text-[9px] font-mono text-slate-400 mt-0.5">${votes}/9</span>
            </div>
          </td>
        `;
      });

      const ensembleAcc = (ensembleCorrectCount / 6 * 100).toFixed(0);
      footHtml += `<td class="py-2.5 px-3 text-right text-emerald-400 font-mono text-sm">${ensembleAcc}%</td></tr>`;
      tfoot.innerHTML = footHtml;

      lucide.createIcons();
    }


    /* ---------------------------------------------------------------------- */
    /* 9. SLIDE 9: SHAP BEESWARM PLOT                                         */
    /* ---------------------------------------------------------------------- */
    const shapData = [
      {
        feature: 'worst concave points',
        points: [
          { val: 0.95, shap: 0.62 }, { val: 0.88, shap: 0.55 }, { val: 0.92, shap: 0.58 },
          { val: 0.75, shap: 0.42 }, { val: 0.80, shap: 0.48 }, { val: 0.70, shap: 0.35 },
          { val: 0.55, shap: 0.15 }, { val: 0.50, shap: 0.05 }, { val: 0.45, shap: -0.08 },
          { val: 0.30, shap: -0.28 }, { val: 0.20, shap: -0.42 }, { val: 0.15, shap: -0.50 },
          { val: 0.10, shap: -0.58 }, { val: 0.05, shap: -0.65 }
        ]
      },
      {
        feature: 'worst perimeter',
        points: [
          { val: 0.90, shap: 0.50 }, { val: 0.85, shap: 0.45 }, { val: 0.80, shap: 0.38 },
          { val: 0.65, shap: 0.22 }, { val: 0.60, shap: 0.18 }, { val: 0.50, shap: 0.02 },
          { val: 0.40, shap: -0.15 }, { val: 0.35, shap: -0.25 }, { val: 0.25, shap: -0.38 },
          { val: 0.15, shap: -0.48 }, { val: 0.08, shap: -0.55 }
        ]
      },
      {
        feature: 'mean radius',
        points: [
          { val: 0.92, shap: 0.40 }, { val: 0.82, shap: 0.32 }, { val: 0.75, shap: 0.24 },
          { val: 0.60, shap: 0.10 }, { val: 0.50, shap: -0.02 }, { val: 0.38, shap: -0.18 },
          { val: 0.28, shap: -0.30 }, { val: 0.12, shap: -0.45 }
        ]
      },
      {
        feature: 'texture error',
        points: [
          { val: 0.90, shap: 0.04 }, { val: 0.80, shap: -0.03 }, { val: 0.70, shap: 0.02 },
          { val: 0.60, shap: -0.02 }, { val: 0.50, shap: 0.01 }, { val: 0.40, shap: -0.01 },
          { val: 0.30, shap: 0.03 }, { val: 0.20, shap: -0.04 }, { val: 0.10, shap: 0.01 }
        ]
      }
    ];

    function filterShapPoints(filterType) {
      document.getElementById('shap-btn-all').className = filterType === 'all' ? 'px-2 py-0.5 rounded bg-slate-800 text-slate-200' : 'px-2 py-0.5 rounded text-slate-400 hover:bg-slate-800';
      document.getElementById('shap-btn-high').className = filterType === 'high' ? 'px-2 py-0.5 rounded bg-rose-950 text-rose-300 font-bold' : 'px-2 py-0.5 rounded text-rose-400 hover:bg-slate-800';
      document.getElementById('shap-btn-low').className = filterType === 'low' ? 'px-2 py-0.5 rounded bg-blue-950 text-blue-300 font-bold' : 'px-2 py-0.5 rounded text-blue-400 hover:bg-slate-800';

      const dots = document.querySelectorAll('.shap-dot');
      dots.forEach((dot) => {
        const val = parseFloat(dot.getAttribute('data-val'));
        if (filterType === 'all') {
          dot.style.opacity = '1';
          dot.style.transform = 'scale(1)';
        } else if (filterType === 'high') {
          if (val > 0.5) {
            dot.style.opacity = '1';
            dot.style.transform = 'scale(1.25)';
          } else {
            dot.style.opacity = '0.15';
            dot.style.transform = 'scale(0.8)';
          }
        } else if (filterType === 'low') {
          if (val <= 0.5) {
            dot.style.opacity = '1';
            dot.style.transform = 'scale(1.25)';
          } else {
            dot.style.opacity = '0.15';
            dot.style.transform = 'scale(0.8)';
          }
        }
      });
    }

    function initSlide9ShapPlot() {
      const rows = document.querySelectorAll('.shap-row');
      const tooltip = document.getElementById('shap-tooltip');

      rows.forEach((rowElem) => {
        const featName = rowElem.getAttribute('data-feature');
        const featObj = shapData.find(d => d.feature === featName);
        if (!featObj) return;

        rowElem.innerHTML = '';

        featObj.points.forEach((pt) => {
          const dot = document.createElement('div');
          const leftPercent = ((pt.shap + 0.7) / 1.4) * 100;

          let color = '#3b82f6';
          if (pt.val > 0.65) color = '#f43f5e';
          else if (pt.val > 0.4) color = '#a855f7';

          const jitterY = (Math.random() - 0.5) * 12;

          dot.className = 'shap-dot absolute w-3 h-3 rounded-full cursor-pointer transition-all hover:scale-150 border border-slate-950';
          dot.setAttribute('data-val', pt.val);
          dot.setAttribute('data-shap', pt.shap);
          dot.style.left = `${leftPercent}%`;
          dot.style.top = `calc(50% + ${jitterY}px)`;
          dot.style.backgroundColor = color;
          dot.style.boxShadow = `0 0 6px ${color}80`;

          dot.addEventListener('mouseenter', (e) => {
            const rect = dot.getBoundingClientRect();
            const containerRect = document.getElementById('shap-beeswarm-container').getBoundingClientRect();
            tooltip.classList.remove('hidden');
            tooltip.style.left = `${rect.left - containerRect.left + 15}px`;
            tooltip.style.top = `${rect.top - containerRect.top - 10}px`;

            const impactText = pt.shap > 0 
              ? `<span class="text-rose-400 font-bold">&phi; = +${pt.shap.toFixed(2)} (Hacia Maligno)</span>` 
              : `<span class="text-cyan-400 font-bold">&phi; = ${pt.shap.toFixed(2)} (Hacia Benigno)</span>`;

            tooltip.innerHTML = `
              <div class="text-[10px] text-slate-400 uppercase font-mono">${featName}</div>
              <div>Valor de la Muestra: <strong class="text-white">${pt.val > 0.5 ? 'Alto (Rojo)' : 'Bajo (Azul)'}</strong></div>
              <div>Valor Shapley: ${impactText}</div>
            `;
          });

          dot.addEventListener('mouseleave', () => {
            tooltip.classList.add('hidden');
          });

          rowElem.appendChild(dot);
        });
      });
    }


    /* ---------------------------------------------------------------------- */
    /* 10. SLIDE 11: EXTRAPOLATION LIVE CHART (CHART.JS)                      */
    /* ---------------------------------------------------------------------- */
    let extrapolationChartInstance = null;

    function initSlide11ExtrapolationChart() {
      const ctx = document.getElementById('extrapolationChart');
      if (!ctx) return;

      if (extrapolationChartInstance) {
        extrapolationChartInstance.destroy();
      }

      const trainPoints = [];
      const futureRealPoints = [];
      const linearFit = [];
      const randomForestFit = [];

      let maxTrainY = -Infinity;

      for (let x = 0; x <= 12; x += 0.5) {
        const noise = (Math.random() - 0.5) * 1.5;
        const yTrue = 1.9 * x + 4 + noise;

        if (x <= 7.0) {
          trainPoints.push({ x: x, y: yTrue });
          if (yTrue > maxTrainY) maxTrainY = yTrue;
        } else {
          futureRealPoints.push({ x: x, y: yTrue });
        }

        linearFit.push({ x: x, y: 1.9 * x + 4 });

        if (x <= 7.0) {
          randomForestFit.push({ x: x, y: 1.9 * x + 4 + (Math.sin(x * 2) * 0.35) });
        } else {
          randomForestFit.push({ x: x, y: maxTrainY });
        }
      }

      extrapolationChartInstance = new Chart(ctx, {
        type: 'line',
        data: {
          datasets: [
            {
              label: 'Datos de Entrenamiento (X ∈ [0, 7])',
              data: trainPoints,
              type: 'scatter',
              backgroundColor: '#22d3ee',
              pointRadius: 4.5,
              order: 3
            },
            {
              label: 'Futuro / Zona Oculta (X ∈ (7, 12])',
              data: futureRealPoints,
              type: 'scatter',
              backgroundColor: 'rgba(148, 163, 184, 0.45)',
              pointRadius: 4,
              order: 4
            },
            {
              label: 'Regresión Lineal (Extrapola Tendencia)',
              data: linearFit,
              borderColor: '#38bdf8',
              borderWidth: 2.5,
              borderDash: [5, 5],
              fill: false,
              pointRadius: 0,
              tension: 0,
              order: 2
            },
            {
              label: 'Random Forest (Meseta Horizontal a partir de X = 7)',
              data: randomForestFit,
              borderColor: '#fb7185',
              borderWidth: 3.5,
              fill: false,
              pointRadius: 0,
              tension: 0,
              order: 1
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          animation: { duration: 600 },
          scales: {
            x: {
              type: 'linear',
              position: 'bottom',
              min: 0,
              max: 12,
              grid: { color: 'rgba(51, 65, 85, 0.4)' },
              ticks: { color: '#94a3b8', font: { family: 'monospace' } },
              title: { display: true, text: 'Variable X (Tiempo / Espacio)', color: '#94a3b8' }
            },
            y: {
              min: 0,
              max: 30,
              grid: { color: 'rgba(51, 65, 85, 0.4)' },
              ticks: { color: '#94a3b8', font: { family: 'monospace' } },
              title: { display: true, text: 'Variable Objetivo Y', color: '#94a3b8' }
            }
          },
          plugins: {
            legend: {
              labels: { color: '#e2e8f0', font: { family: 'monospace', size: 11 } }
            },
            tooltip: {
              backgroundColor: '#0f172a',
              titleColor: '#34d399',
              bodyFont: { family: 'monospace' }
            }
          }
        }
      });
    }

    function regenerateExtrapolationData() {
      initSlide11ExtrapolationChart();
    }


    /* ---------------------------------------------------------------------- */
    /* 11. SLIDE 13: CPU PARALLEL ANIMATION                                   */
    /* ---------------------------------------------------------------------- */
    function triggerCPULoadAnimation() {
      const bars = document.querySelectorAll('.core-bar');
      bars.forEach(b => { b.style.width = '0%'; });
      setTimeout(() => {
        bars.forEach((b, idx) => {
          setTimeout(() => {
            b.style.width = '96%';
          }, idx * 110);
        });
      }, 80);
    }


    /* ---------------------------------------------------------------------- */
    /* 12. SLIDE 15: QUIZ EVALUATION                                          */
    /* ---------------------------------------------------------------------- */
    function runQuizEvaluation() {
      const q1 = document.getElementById('quiz-q1').value;
      const q2 = document.getElementById('quiz-q2').value;
      const q3 = document.getElementById('quiz-q3').value;

      const resultBox = document.getElementById('quiz-result-box');
      const titleElem = document.getElementById('quiz-verdict-title');
      const descElem = document.getElementById('quiz-verdict-desc');

      if (q2 === 'yes') {
        resultBox.className = 'p-4 rounded-xl bg-rose-950/40 border border-rose-500/50 flex items-center justify-between';
        titleElem.className = 'text-base font-bold font-mono text-rose-400';
        titleElem.innerHTML = '⚠️ NO RECOMENDADO: SERIE TEMPORAL CON TENDENCIA';
        descElem.textContent = 'Random Forest se aplanará horizontalmente y fallará al extrapolar valores superiores a max(Y_train). Utiliza modelos lineales, ARIMA o redes autorregresivas.';
      } else if (q1 === 'text' || q1 === 'image') {
        resultBox.className = 'p-4 rounded-xl bg-amber-950/40 border border-amber-500/50 flex items-center justify-between';
        titleElem.className = 'text-base font-bold font-mono text-amber-400';
        titleElem.innerHTML = '⚠️ NO RECOMENDADO: DATOS NO ESTRUCTURADOS / DISPERSOS';
        descElem.textContent = 'Los bosques sufren en matrices dispersas de alta dimensionalidad (50,000+ columnas). Utiliza Transformers o modelos lineales regularizados.';
      } else if (q3 === 'edge') {
        resultBox.className = 'p-4 rounded-xl bg-amber-950/40 border border-amber-500/50 flex items-center justify-between';
        titleElem.className = 'text-base font-bold font-mono text-amber-400';
        titleElem.innerHTML = '⚠️ PRECAUCIÓN: RESTRICCIÓN EXTREMA DE RAM (< 2 MB)';
        descElem.textContent = 'Los árboles en memoria consumen un espacio significativo en microcontroladores. Si requieres inferencia ultra-ligera en el edge, un modelo lineal o árbol podado es mejor.';
      } else {
        resultBox.className = 'p-4 rounded-xl bg-emerald-950/40 border border-emerald-500/40 flex items-center justify-between';
        titleElem.className = 'text-base font-bold font-mono text-emerald-400';
        titleElem.innerHTML = '✓ RANDOM FOREST ES TU ELECCIÓN ÓPTIMA';
        descElem.textContent = 'Datos tabulares heterogéneos sin extrapolación. Obtendrás un modelo con mínima necesidad de ajuste, nulo riesgo de sobreajuste severo y paralelismo nativo.';
      }
    }


    /* ---------------------------------------------------------------------- */
    /* 13. DOM READY INITIALIZATION                                           */
    /* ---------------------------------------------------------------------- */
    window.addEventListener('DOMContentLoaded', () => {
      initDots();
      updateNavigationUI();
      lucide.createIcons();
      onSlideEnter(1);
    });

  </script>
</body>
</html>
'''

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated enhanced 15-slide index.html. Total size: {len(html_content)} bytes.")
