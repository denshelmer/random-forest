# -*- coding: utf-8 -*-
"""
Builds the theory-first 12-slide presentation based on the exact user text and curriculum.
Theory is front and center; examples are short, direct, and illustrative.
"""

import sys

html_content = r'''<!DOCTYPE html>
<html lang="es" class="dark scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bosques Aleatorios (Random Forest) | Teoría, Fundamentos y Criterio Técnico</title>
  
  <!-- Tailwind CSS v3 via CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          colors: {
            brand: {
              dark: '#020617',
              card: '#0b1329',
              accent: '#10b981',
              cyan: '#06b6d4',
              amber: '#f59e0b',
              rose: '#f43f5e',
              indigo: '#6366f1'
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

  <!-- Lucide Icons via CDN -->
  <script src="https://unpkg.com/lucide@latest"></script>

  <style>
    /* Custom Scrollbar */
    ::-webkit-scrollbar {
      width: 7px;
      height: 7px;
    }
    ::-webkit-scrollbar-track {
      background: #020617;
    }
    ::-webkit-scrollbar-thumb {
      background: #1e293b;
      border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: #10b981;
    }
    .glass-card {
      background: rgba(15, 23, 42, 0.85);
      backdrop-filter: blur(16px);
      border: 1px solid rgba(51, 65, 85, 0.65);
    }
    .text-glow-emerald {
      text-shadow: 0 0 20px rgba(52, 211, 153, 0.5);
    }
    .text-glow-cyan {
      text-shadow: 0 0 20px rgba(34, 211, 238, 0.5);
    }
    .bg-grid-pattern {
      background-size: 28px 28px;
      background-image: 
        radial-gradient(circle, rgba(71, 85, 105, 0.28) 1.2px, transparent 1.2px);
    }
    .slide-section {
      display: none;
      opacity: 0;
      width: 100%;
    }
    .slide-section.active {
      display: block;
      opacity: 1;
    }
    .objective-card {
      background: linear-gradient(135deg, rgba(16, 185, 129, 0.09) 0%, rgba(6, 182, 212, 0.06) 100%);
      border: 1px solid rgba(16, 185, 129, 0.35);
      box-shadow: 0 4px 20px -2px rgba(16, 185, 129, 0.1);
    }
    .theory-card {
      background: linear-gradient(135deg, rgba(15, 23, 42, 0.9) 0%, rgba(30, 41, 59, 0.75) 100%);
      border: 1px solid rgba(56, 189, 248, 0.28);
    }
    .example-card {
      background: linear-gradient(135deg, rgba(30, 41, 59, 0.85) 0%, rgba(15, 23, 42, 0.95) 100%);
      border: 1px solid rgba(16, 185, 129, 0.3);
    }
    .takeaway-card {
      background: linear-gradient(135deg, rgba(251, 191, 36, 0.08) 0%, rgba(15, 23, 42, 0.85) 100%);
      border: 1px solid rgba(251, 191, 36, 0.32);
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
        <span>EXPOSICIÓN: RANDOM FOREST</span>
      </div>
      <span class="text-slate-600 text-xs hidden sm:inline">|</span>
      <h1 class="text-xs md:text-sm font-semibold text-slate-300 tracking-tight hidden sm:block truncate max-w-md">
        Fundamentos Teóricos, Puntos Críticos y Criterio
      </h1>
    </div>

    <!-- Center Slide Topic Badge -->
    <div id="header-slide-topic" class="text-xs font-mono text-cyan-400 px-3.5 py-1 rounded-lg bg-slate-900 border border-slate-800 hidden md:block">
      1. Portada & Mapa de Ruta
    </div>

    <div class="flex items-center gap-2">
      <!-- Toggle Speaker Notes Drawer Button -->
      <button id="btn-speaker-notes" onclick="toggleSpeakerNotes()" title="Guión y Notas del Expositor (N)" class="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-cyan-950/70 hover:bg-cyan-900 border border-cyan-500/40 text-cyan-300 text-xs font-mono transition">
        <i data-lucide="mic" class="w-3.5 h-3.5 text-cyan-400"></i>
        <span class="hidden sm:inline">Guión Expositor</span>
        <kbd class="text-[10px] bg-slate-900 px-1.5 py-0.5 rounded border border-cyan-700/50">N</kbd>
      </button>

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
        <span id="header-counter-current" class="text-emerald-400 font-bold">1</span> / <span id="header-counter-total">12</span>
      </div>
    </div>
  </header>

  <!-- LINEAR PROGRESS BAR -->
  <div class="fixed top-[45px] left-0 w-full h-[3px] bg-slate-900 z-50">
    <div id="progress-bar-fill" class="h-full bg-gradient-to-r from-emerald-500 via-cyan-400 to-emerald-400 w-[8.33%] transition-all duration-300"></div>
  </div>

  <!-- ==================================================================== -->
  <!-- SPEAKER NOTES DRAWER (SLIDE-OVER FOR ORAL PRESENTATION)               -->
  <!-- ==================================================================== -->
  <aside id="speaker-notes-drawer" class="fixed top-[48px] right-0 bottom-0 w-full sm:w-[480px] bg-slate-950/95 backdrop-blur-xl border-l border-slate-800 z-40 transform translate-x-full transition-transform duration-300 shadow-2xl flex flex-col justify-between overflow-y-auto">
    <div class="p-6 space-y-5">
      <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2 text-cyan-400 font-mono text-xs font-bold uppercase tracking-wider">
          <i data-lucide="mic" class="w-4 h-4 text-cyan-400"></i>
          <span>Guión de Exposición Oral</span>
        </div>
        <button onclick="toggleSpeakerNotes()" class="p-1 rounded-lg bg-slate-900 hover:bg-slate-800 text-slate-400 hover:text-white">
          <i data-lucide="x" class="w-4 h-4"></i>
        </button>
      </div>

      <!-- Current Slide Info in Drawer -->
      <div class="space-y-1">
        <span id="drawer-slide-num" class="text-[11px] font-mono text-emerald-400 uppercase tracking-widest font-bold">DIAPOSITIVA 1</span>
        <h3 id="drawer-slide-title" class="text-base font-bold text-white">Portada & Mapa de Ruta</h3>
      </div>

      <!-- Slide Objective in Drawer -->
      <div class="p-3.5 rounded-xl bg-emerald-950/30 border border-emerald-500/30 space-y-1">
        <span class="text-[10px] font-mono uppercase tracking-wider text-emerald-400 font-bold block">🎯 Objetivo de la Diapositiva:</span>
        <p id="drawer-slide-objective" class="text-xs text-slate-200 leading-relaxed font-sans"></p>
      </div>

      <!-- What to say out loud (Speech Script) -->
      <div class="space-y-2">
        <div class="flex items-center gap-1.5 text-xs font-mono text-cyan-300 font-semibold">
          <i data-lucide="volume-2" class="w-3.5 h-3.5 text-cyan-400"></i>
          <span>Lo que dices en voz alta al público:</span>
        </div>
        <div id="drawer-slide-script" class="p-4 rounded-xl bg-slate-900/90 border border-slate-800 text-xs sm:text-sm text-slate-200 leading-relaxed font-sans space-y-3">
        </div>
      </div>

      <!-- Interaction & Demonstration Tips -->
      <div class="p-3.5 rounded-xl bg-amber-950/20 border border-amber-500/30 space-y-1.5">
        <span class="text-[10px] font-mono uppercase tracking-wider text-amber-400 font-bold flex items-center gap-1">
          <i data-lucide="sparkles" class="w-3 h-3 text-amber-400"></i>
          <span>Consejo Pedagógico para la Exposición:</span>
        </span>
        <p id="drawer-slide-tips" class="text-xs text-amber-200/90 leading-relaxed font-sans"></p>
      </div>
    </div>

    <div class="p-4 border-t border-slate-800 bg-slate-950 text-center text-[11px] font-mono text-slate-500">
      Presiona <kbd class="px-1.5 py-0.5 rounded bg-slate-900 border border-slate-700 text-slate-300">N</kbd> o <kbd class="px-1.5 py-0.5 rounded bg-slate-900 border border-slate-700 text-slate-300">Esc</kbd> para ocultar este panel.
    </div>
  </aside>

  <!-- ==================================================================== -->
  <!-- MAIN PRESENTATION VIEWPORT                                           -->
  <!-- ==================================================================== -->
  <main class="w-full max-w-6xl mx-auto px-4 md:px-8 pt-16 pb-24 flex-grow flex flex-col justify-center relative bg-grid-pattern min-h-[calc(100vh-80px)]">

    <!-- ==================================================================== -->
    <!-- SLIDE 1: PORTADA & MAPA DE RUTA                                      -->
    <!-- ==================================================================== -->
    <section id="slide-1" class="slide-section active py-8">
      <div class="min-h-[75vh] flex flex-col justify-between space-y-8 relative">
        <div class="absolute -top-10 left-1/2 -translate-x-1/2 w-[520px] h-[340px] bg-emerald-500/10 rounded-full blur-3xl pointer-events-none -z-10 animate-pulse"></div>

        <div class="text-center space-y-4 pt-4">
          <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-slate-900/90 border border-emerald-500/40 text-emerald-400 text-xs font-mono font-semibold tracking-wider uppercase mb-2 shadow-lg shadow-emerald-950/40">
            <i data-lucide="sparkles" class="w-4 h-4 text-emerald-400"></i>
            <span>Presentación Teórica & Criterio de Selección</span>
          </div>

          <h1 class="text-4xl sm:text-6xl lg:text-7xl font-black tracking-tight text-white leading-tight">
            Bosques Aleatorios<br>
            <span class="bg-gradient-to-r from-emerald-400 via-cyan-300 to-teal-400 bg-clip-text text-transparent text-glow-emerald">
              (Random Forest)
            </span>
          </h1>

          <p class="text-sm sm:text-lg text-slate-300 font-light max-w-3xl mx-auto leading-relaxed">
            Introducción, Fundamentos Teóricos, Puntos Críticos y Criterio de Decisión
          </p>

          <div class="pt-1">
            <span class="text-xs sm:text-sm font-mono text-cyan-400 tracking-widest uppercase bg-cyan-950/60 px-4 py-1.5 rounded-full border border-cyan-500/30">
              Autor: Denshel David Mérida Quispe
            </span>
          </div>
        </div>

        <!-- Objective Banner -->
        <div class="objective-card p-4 rounded-2xl flex items-start gap-3.5 max-w-4xl mx-auto w-full">
          <div class="w-9 h-9 rounded-xl bg-emerald-500/20 border border-emerald-500/40 flex items-center justify-center text-emerald-400 shrink-0 mt-0.5">
            <i data-lucide="target" class="w-5 h-5 text-emerald-400"></i>
          </div>
          <div class="space-y-1">
            <span class="text-[11px] font-mono uppercase tracking-wider text-emerald-400 font-bold block">🎯 Objetivo General de la Exposición:</span>
            <p class="text-xs sm:text-sm text-slate-200 leading-relaxed font-sans">
              Comprender qué es Random Forest, por qué surge ante la inestabilidad del árbol individual, cómo operan sus tres pilares teóricos (Condorcet, Bagging y Subespacio), analizar un ejemplo ilustrativo directo y dominar sus criterios técnicos críticos (SHAP, extrapolación y hardware).
            </p>
          </div>
        </div>

        <!-- 6 Theoretical Topics Navigation -->
        <div class="max-w-4xl mx-auto w-full space-y-3">
          <span class="text-xs font-mono text-slate-400 uppercase tracking-wider block text-center">
            Estructura de la Exposición en 6 Módulos Teóricos:
          </span>
          <div class="grid grid-cols-2 sm:grid-cols-3 gap-2.5 text-xs font-mono">
            <button onclick="goToSlide(2)" class="p-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-left text-slate-300 transition">
              <span class="text-cyan-400 font-bold block">1. Contexto General</span>
              <span class="text-[11px] text-slate-400">¿Qué es y analogía del comité?</span>
            </button>
            <button onclick="goToSlide(3)" class="p-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-left text-slate-300 transition">
              <span class="text-cyan-400 font-bold block">2. El Problema</span>
              <span class="text-[11px] text-slate-400">Inestabilidad del árbol solitario</span>
            </button>
            <button onclick="goToSlide(4)" class="p-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-left text-slate-300 transition">
              <span class="text-emerald-400 font-bold block">3. Los Tres Pilares</span>
              <span class="text-[11px] text-slate-400">Condorcet, Bagging y Subespacio</span>
            </button>
            <button onclick="goToSlide(7)" class="p-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-left text-slate-300 transition">
              <span class="text-emerald-400 font-bold block">4. Ejemplo Práctico</span>
              <span class="text-[11px] text-slate-400">Señales de cruce peatonal</span>
            </button>
            <button onclick="goToSlide(8)" class="p-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-left text-slate-300 transition">
              <span class="text-rose-400 font-bold block">5. Criterios Técnicos</span>
              <span class="text-[11px] text-slate-400">SHAP, Extrapolación y ONNX</span>
            </button>
            <button onclick="goToSlide(11)" class="p-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-left text-slate-300 transition">
              <span class="text-amber-400 font-bold block">6. Matriz de Decisión</span>
              <span class="text-[11px] text-slate-400">Cuándo SÍ vs Cuándo NO</span>
            </button>
          </div>
        </div>

        <!-- Launch Presentation Action Bar -->
        <div class="flex flex-col sm:flex-row items-center justify-center gap-3 pt-2">
          <button onclick="goToSlide(2)" class="w-full sm:w-auto px-7 py-3.5 rounded-xl bg-gradient-to-r from-emerald-500 to-teal-500 hover:from-emerald-400 text-slate-950 font-mono text-sm font-bold tracking-wide flex items-center justify-center gap-3 transition transform hover:scale-105 shadow-xl shadow-emerald-500/25">
            <span>Iniciar Exposición</span>
            <i data-lucide="arrow-right" class="w-4 h-4"></i>
          </button>
          <button onclick="toggleSpeakerNotes()" class="w-full sm:w-auto px-5 py-3.5 rounded-xl bg-slate-900 hover:bg-slate-800 text-cyan-300 border border-slate-700 font-mono text-xs font-semibold flex items-center justify-center gap-2 transition">
            <i data-lucide="mic" class="w-4 h-4 text-cyan-400"></i>
            <span>Ver Guión del Expositor [N]</span>
          </button>
        </div>
      </div>
    </section>

    <!-- ==================================================================== -->
    <!-- SLIDE 2: 1. ¿QUÉ ES RANDOM FOREST? (CONTEXTO GENERAL)                -->
    <!-- ==================================================================== -->
    <section id="slide-2" class="slide-section py-4">
      <div class="space-y-4">
        <!-- Title and Badges -->
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-2 border-b border-slate-800 pb-3">
          <div>
            <div class="text-xs font-mono text-cyan-400 uppercase tracking-wider font-semibold">1. Contexto General &bull; Aprendizaje en Ensamble</div>
            <h2 class="text-2xl md:text-3xl font-extrabold text-white">
              ¿Qué es Random Forest?
            </h2>
          </div>
          <div class="px-3 py-1.5 rounded-lg bg-cyan-950/70 border border-cyan-500/40 text-cyan-300 font-mono text-xs">
            Ensemble Learning &bull; Voto Mayoritario
          </div>
        </div>

        <!-- Slide Objective Banner -->
        <div class="objective-card p-3.5 rounded-xl flex items-start gap-3">
          <div class="w-8 h-8 rounded-lg bg-emerald-500/20 border border-emerald-500/40 flex items-center justify-center text-emerald-400 shrink-0 mt-0.5">
            <i data-lucide="target" class="w-4 h-4 text-emerald-400"></i>
          </div>
          <div>
            <span class="text-[11px] font-mono uppercase tracking-wider text-emerald-400 font-bold block">🎯 Objetivo de la Diapositiva:</span>
            <p class="text-xs sm:text-sm text-slate-200 leading-relaxed font-sans">
              Comprender el principio de ensamble (combinación de múltiples modelos) y visualizar su intuición mediante la analogía médica del comité de expertos frente al especialista solitario.
            </p>
          </div>
        </div>

        <!-- Main Content Grid: Theory (60%) + Short Direct Example (40%) -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          
          <!-- Theory Card -->
          <div class="lg:col-span-7 theory-card p-5 rounded-2xl space-y-4">
            <h3 class="text-xs font-mono text-cyan-400 uppercase tracking-wider font-bold flex items-center gap-2">
              <i data-lucide="book-open" class="w-4 h-4 text-cyan-400"></i>
              Fundamento Conceptual
            </h3>

            <div class="space-y-3.5 text-xs sm:text-sm text-slate-300 leading-relaxed font-sans">
              <p>
                <strong class="text-white">Random Forest (Bosque Aleatorio)</strong> es uno de los algoritmos más populares, efectivos y utilizados en el Aprendizaje Automático (<em>Machine Learning</em>).
              </p>

              <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2">
                <span class="text-xs font-mono text-cyan-300 font-bold block">&bull; Aprendizaje en Ensamble (Ensemble Learning):</span>
                <p class="text-xs text-slate-300">
                  Su principio es sencillo: en lugar de confiar en la predicción de un único modelo, combina las respuestas de decenas o cientos de modelos individuales (en este caso, <strong class="text-white">árboles de decisión</strong>) para obtener un resultado final mucho más <strong class="text-emerald-400 font-bold">preciso, estable y confiable</strong>.
                </p>
              </div>

              <div class="p-3.5 rounded-xl bg-cyan-950/30 border border-cyan-500/30 space-y-2">
                <span class="text-xs font-mono text-cyan-300 font-bold flex items-center gap-1.5">
                  <i data-lucide="users" class="w-4 h-4 text-cyan-400"></i>
                  La Analogía del Comité de Expertos:
                </span>
                <p class="text-xs text-slate-300">
                  Si tienes que tomar una decisión médica compleja, pedir la opinión de un solo especialista puede ser riesgoso si esa persona tiene un mal día o un sesgo particular. Es mucho más seguro consultar a un panel de <strong>100 especialistas independientes</strong> y tomar la decisión final por <strong>votación de la mayoría</strong>.
                </p>
                <p class="text-[11px] font-mono text-cyan-300">
                  &rarr; Eso es exactamente lo que hace Random Forest con los árboles de decisión.
                </p>
              </div>
            </div>
          </div>

          <!-- Short Direct Illustration -->
          <div class="lg:col-span-5 example-card p-5 rounded-2xl space-y-4">
            <h3 class="text-xs font-mono text-emerald-400 uppercase tracking-wider font-bold flex items-center gap-2">
              <i data-lucide="compass" class="w-4 h-4 text-emerald-400"></i>
              Ilustración Visual del Ensamble
            </h3>

            <div class="space-y-3">
              <!-- Solo Doctor -->
              <div class="p-3 rounded-xl bg-rose-950/20 border border-rose-500/30 space-y-1">
                <div class="flex items-center justify-between text-xs font-mono">
                  <span class="text-rose-400 font-bold">1 Especialista Solitario:</span>
                  <span class="text-rose-400 bg-rose-950 px-2 py-0.5 rounded text-[10px]">Alta Incertidumbre</span>
                </div>
                <p class="text-[11px] text-slate-400">
                  Vulnerable a sesgos particulares, cansancio o errores de diagnóstico aislados.
                </p>
              </div>

              <!-- Down arrow icon -->
              <div class="text-center text-slate-600 font-mono text-xs">
                &darr; Frente a la solución colectiva &darr;
              </div>

              <!-- Committee of 100 -->
              <div class="p-3.5 rounded-xl bg-emerald-950/30 border border-emerald-500/40 space-y-2">
                <div class="flex items-center justify-between text-xs font-mono">
                  <span class="text-emerald-400 font-bold">Panel de 100 Especialistas:</span>
                  <span class="text-emerald-400 bg-emerald-950 px-2 py-0.5 rounded text-[10px]">Consenso Robusto</span>
                </div>
                <p class="text-[11px] text-slate-300">
                  Cada especialista emite un voto independiente. Los errores aislados se cancelan entre sí y la verdad converge por mayoría.
                </p>
                <div class="flex items-center justify-between text-[11px] font-mono text-emerald-300 pt-1 border-t border-emerald-500/20">
                  <span>Resultado del consenso:</span>
                  <strong class="text-white">Confianza Máxima</strong>
                </div>
              </div>
            </div>

            <!-- Takeaway Card -->
            <div class="takeaway-card p-3 rounded-xl space-y-1">
              <span class="text-[10px] font-mono uppercase tracking-wider text-amber-400 font-bold block">💡 Conclusión Clave:</span>
              <p class="text-[11px] text-amber-200 leading-snug">
                Random Forest no reemplaza al árbol de decisión: lo multiplica y democratiza para eliminar el riesgo del error individual.
              </p>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- ==================================================================== -->
    <!-- SLIDE 3: 2. EL PROBLEMA: INESTABILIDAD DEL ÁRBOL INDIVIDUAL          -->
    <!-- ==================================================================== -->
    <section id="slide-3" class="slide-section py-4">
      <div class="space-y-4">
        <!-- Title -->
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-2 border-b border-slate-800 pb-3">
          <div>
            <div class="text-xs font-mono text-rose-400 uppercase tracking-wider font-semibold">2. El Problema que Resuelve &bull; Fallo Estructural</div>
            <h2 class="text-2xl md:text-3xl font-extrabold text-white">
              La Inestabilidad del Árbol Individual
            </h2>
          </div>
          <div class="text-xs font-mono text-rose-300 bg-rose-950 px-3 py-1.5 rounded-lg border border-rose-500/40">
            Alta Varianza &bull; Sobreajuste (Overfitting)
          </div>
        </div>

        <!-- Slide Objective Banner -->
        <div class="objective-card p-3.5 rounded-xl flex items-start gap-3">
          <div class="w-8 h-8 rounded-lg bg-emerald-500/20 border border-emerald-500/40 flex items-center justify-center text-emerald-400 shrink-0 mt-0.5">
            <i data-lucide="target" class="w-4 h-4 text-emerald-400"></i>
          </div>
          <div>
            <span class="text-[11px] font-mono uppercase tracking-wider text-emerald-400 font-bold block">🎯 Objetivo de la Diapositiva:</span>
            <p class="text-xs sm:text-sm text-slate-200 leading-relaxed font-sans">
              Identificar la causa del nacimiento de Random Forest: la fragilidad y tendencia al sobreajuste de los árboles profundos, y cómo promediar muchos árboles disuelve la inestabilidad.
            </p>
          </div>
        </div>

        <!-- Main Content Grid -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          
          <!-- Theory Card -->
          <div class="lg:col-span-7 theory-card p-5 rounded-2xl space-y-4">
            <h3 class="text-xs font-mono text-rose-400 uppercase tracking-wider font-bold flex items-center gap-2">
              <i data-lucide="alert-triangle" class="w-4 h-4 text-rose-400"></i>
              Para entender el bosque, primero hay que entender el fallo del árbol
            </h3>

            <div class="space-y-3.5 text-xs sm:text-sm text-slate-300 leading-relaxed font-sans">
              <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-1">
                <strong class="text-white block font-mono text-xs">&bull; ¿Cómo piensa un Árbol de Decisión?</strong>
                <p class="text-slate-300 text-xs">
                  Divide los datos con preguntas simples de tipo Sí/No (por ejemplo: <em>¿El tumor mide más de 2 cm? ¿Tiene forma irregular?</em>). Va creando ramas hasta llegar a una conclusión en las hojas.
                </p>
              </div>

              <div class="p-3.5 rounded-xl bg-rose-950/20 border border-rose-500/30 space-y-1.5">
                <strong class="text-rose-400 block font-mono text-xs">&bull; El Gran Defecto: Alta Varianza (Sobreajuste / Overfitting):</strong>
                <p class="text-xs text-slate-300">
                  Un árbol de decisión profundo tiene una tendencia natural a <strong>memorizar los datos de entrenamiento</strong>, incluyendo el ruido y las anomalías estadísticas.
                </p>
              </div>

              <div class="p-3.5 rounded-xl bg-amber-950/20 border border-amber-500/30 space-y-1.5">
                <strong class="text-amber-400 block font-mono text-xs">&bull; Inestabilidad Estructural:</strong>
                <p class="text-xs text-slate-300">
                  Si cambias apenas un par de datos en el entrenamiento, la estructura de todo el árbol puede cambiar de arriba a abajo. Es un modelo con <strong>poco sesgo</strong> (aprende bien), pero <strong>muy inestable (alta varianza)</strong>.
                </p>
              </div>
            </div>
          </div>

          <!-- Direct Solution Card -->
          <div class="lg:col-span-5 example-card p-5 rounded-2xl space-y-4">
            <h3 class="text-xs font-mono text-emerald-400 uppercase tracking-wider font-bold flex items-center gap-2">
              <i data-lucide="check-circle-2" class="w-4 h-4 text-emerald-400"></i>
              La Solución de Random Forest
            </h3>

            <div class="p-4 rounded-xl bg-emerald-950/30 border border-emerald-500/40 space-y-2">
              <span class="text-xs font-mono text-emerald-300 font-bold block uppercase tracking-wide">
                El Principio de Cancelación:
              </span>
              <p class="text-xs text-slate-200 leading-relaxed font-sans">
                Mantener la enorme capacidad de aprendizaje de los árboles de decisión, pero <strong>eliminar su inestabilidad promediando los resultados de muchos árboles diferentes</strong>.
              </p>
              <div class="p-2.5 rounded bg-slate-950 border border-slate-800 text-[11px] font-mono text-cyan-300">
                Poco Sesgo (Árbol) + Varianza Reducida (Ensamble) = Modelo Óptimo
              </div>
            </div>

            <!-- Visual Contrast -->
            <div class="space-y-2 text-xs font-mono">
              <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 flex justify-between items-center text-rose-300">
                <span>1 Árbol Profundo:</span>
                <span class="font-bold">Memoriza Ruido (Overfitting)</span>
              </div>
              <div class="p-2.5 rounded-lg bg-emerald-950 border border-emerald-500/40 flex justify-between items-center text-emerald-300">
                <span>Bosque de 100 Árboles:</span>
                <span class="font-bold">Generaliza con Estabilidad</span>
              </div>
            </div>

            <!-- Takeaway Card -->
            <div class="takeaway-card p-3 rounded-xl space-y-1">
              <span class="text-[10px] font-mono uppercase tracking-wider text-amber-400 font-bold block">💡 Conclusión Clave:</span>
              <p class="text-[11px] text-amber-200 leading-snug">
                El sobreajuste es un defecto del individuo solitario; la sabiduría colectiva disuelve el ruido y rescata la señal verdadera.
              </p>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- ==================================================================== -->
    <!-- SLIDE 4: 3A. PILAR 1: CONDORCET (1785)                               -->
    <!-- ==================================================================== -->
    <section id="slide-4" class="slide-section py-4">
      <div class="space-y-4">
        <!-- Title -->
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-2 border-b border-slate-800 pb-3">
          <div>
            <div class="text-xs font-mono text-cyan-400 uppercase tracking-wider font-semibold">3. ¿Cómo Funciona? &bull; Los Tres Pilares Fundamentales</div>
            <h2 class="text-2xl md:text-3xl font-extrabold text-white">
              Pilar A: La Sabiduría de las Masas (Condorcet, 1785)
            </h2>
          </div>
          <div class="text-xs font-mono text-cyan-300 bg-cyan-950 px-3 py-1.5 rounded-lg border border-cyan-500/40">
            Teorema del Jurado &bull; Mayoría Democrática
          </div>
        </div>

        <!-- Slide Objective Banner -->
        <div class="objective-card p-3.5 rounded-xl flex items-start gap-3">
          <div class="w-8 h-8 rounded-lg bg-emerald-500/20 border border-emerald-500/40 flex items-center justify-center text-emerald-400 shrink-0 mt-0.5">
            <i data-lucide="target" class="w-4 h-4 text-emerald-400"></i>
          </div>
          <div>
            <span class="text-[11px] font-mono uppercase tracking-wider text-emerald-400 font-bold block">🎯 Objetivo de la Diapositiva:</span>
            <p class="text-xs sm:text-sm text-slate-200 leading-relaxed font-sans">
              Comprender la base matemática de por qué la votación de jueces independientes supera al individuo, y analizar la condición de oro: la necesidad estricta de diversidad entre árboles.
            </p>
          </div>
        </div>

        <!-- Main Content Grid -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          
          <!-- Theory Card -->
          <div class="lg:col-span-7 theory-card p-5 rounded-2xl space-y-4">
            <h3 class="text-xs font-mono text-cyan-400 uppercase tracking-wider font-bold flex items-center gap-2">
              <i data-lucide="award" class="w-4 h-4 text-cyan-400"></i>
              El Teorema de Condorcet de 1785
            </h3>

            <div class="space-y-3.5 text-xs sm:text-sm text-slate-300 leading-relaxed font-sans">
              <div class="p-4 rounded-xl bg-slate-900 border-l-4 border-cyan-400 text-slate-200 italic">
                "Si juntas a un grupo de votantes independientes, y cada uno tiene una probabilidad de acertar ligeramente mayor al 50%, la probabilidad de que la mayoría del grupo tome la decisión correcta aumenta conforme agregas más personas."
              </div>

              <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2">
                <span class="text-xs font-mono text-cyan-300 font-bold block">&bull; La Escala Demostrativa de Precisión:</span>
                <ul class="space-y-1.5 text-xs font-mono">
                  <li class="flex justify-between items-center text-slate-300 p-1.5 rounded bg-slate-950">
                    <span>&bull; 1 árbol solo:</span>
                    <strong class="text-slate-100">60% de aciertos</strong>
                  </li>
                  <li class="flex justify-between items-center text-cyan-300 p-1.5 rounded bg-slate-950">
                    <span>&bull; 3 árboles votando:</span>
                    <strong class="text-cyan-300 font-bold">65% de aciertos</strong>
                  </li>
                  <li class="flex justify-between items-center text-emerald-400 p-1.5 rounded bg-slate-950">
                    <span>&bull; 11 árboles votando:</span>
                    <strong class="text-emerald-400 font-bold text-sm">75% de aciertos</strong>
                  </li>
                </ul>
              </div>
            </div>
          </div>

          <!-- Golden Rule Card -->
          <div class="lg:col-span-5 example-card p-5 rounded-2xl space-y-4">
            <h3 class="text-xs font-mono text-amber-400 uppercase tracking-wider font-bold flex items-center gap-2">
              <i data-lucide="shield-alert" class="w-4 h-4 text-amber-400"></i>
              La Condición de Oro
            </h3>

            <div class="p-4 rounded-xl bg-amber-950/30 border border-amber-500/40 space-y-2">
              <span class="text-xs font-mono text-amber-300 font-bold block uppercase tracking-wide">
                Exigencia de Diversidad:
              </span>
              <p class="text-xs text-slate-200 leading-relaxed font-sans">
                Los árboles tienen que ser <strong>diferentes entre sí</strong>.
              </p>
              <div class="p-2.5 rounded bg-rose-950/40 border border-rose-500/40 text-[11px] font-mono text-rose-200">
                ⚠️ Si todos los árboles cometen el mismo error, la votación grupal no sirve de absolutamente nada.
              </div>
            </div>

            <div class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs font-mono text-slate-400 space-y-1">
              <span class="text-slate-300 font-bold block">&bull; El desafío para el algoritmo:</span>
              <p class="text-[11px]">
                ¿Cómo logramos que cada árbol aprenda cosas distintas si todos tienen a su disposición la misma base de datos?
              </p>
              <span class="text-cyan-400 font-bold block pt-1">&rarr; Respuesta: Los dos niveles de aleatoriedad (Bagging y Subespacio).</span>
            </div>

            <!-- Takeaway Card -->
            <div class="takeaway-card p-3 rounded-xl space-y-1">
              <span class="text-[10px] font-mono uppercase tracking-wider text-amber-400 font-bold block">💡 Conclusión Clave:</span>
              <p class="text-[11px] text-amber-200 leading-snug">
                La democracia matemática exige independencia: muchos árboles idénticos no son un bosque, son una sola voz repetida.
              </p>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- ==================================================================== -->
    <!-- SLIDE 5: 3B. PILAR 2: BAGGING (MUESTREO CON REEMPLAZO)               -->
    <!-- ==================================================================== -->
    <section id="slide-5" class="slide-section py-4">
      <div class="space-y-4">
        <!-- Title -->
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-2 border-b border-slate-800 pb-3">
          <div>
            <div class="text-xs font-mono text-emerald-400 uppercase tracking-wider font-semibold">3. ¿Cómo Funciona? &bull; Primer Nivel de Aleatoriedad</div>
            <h2 class="text-2xl md:text-3xl font-extrabold text-white">
              Pilar B: Bagging (Muestreo con Reemplazo)
            </h2>
          </div>
          <div class="text-xs font-mono text-emerald-300 bg-emerald-950 px-3 py-1.5 rounded-lg border border-emerald-500/40">
            Bootstrap Aggregating &bull; OOB &approx; 37%
          </div>
        </div>

        <!-- Slide Objective Banner -->
        <div class="objective-card p-3.5 rounded-xl flex items-start gap-3">
          <div class="w-8 h-8 rounded-lg bg-emerald-500/20 border border-emerald-500/40 flex items-center justify-center text-emerald-400 shrink-0 mt-0.5">
            <i data-lucide="target" class="w-4 h-4 text-emerald-400"></i>
          </div>
          <div>
            <span class="text-[11px] font-mono uppercase tracking-wider text-emerald-400 font-bold block">🎯 Objetivo de la Diapositiva:</span>
            <p class="text-xs sm:text-sm text-slate-200 leading-relaxed font-sans">
              Entender el mecanismo de muestreo con reemplazo para diversificar filas de datos y comprender la utilidad del conjunto Out-of-Bag (37%) como examen gratuito de generalización.
            </p>
          </div>
        </div>

        <!-- Main Content Grid -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          
          <!-- Theory Card -->
          <div class="lg:col-span-7 theory-card p-5 rounded-2xl space-y-4">
            <h3 class="text-xs font-mono text-emerald-400 uppercase tracking-wider font-bold flex items-center gap-2">
              <i data-lucide="layers" class="w-4 h-4 text-emerald-400"></i>
              ¿Cómo logramos que cada árbol sea diferente?
            </h3>

            <div class="space-y-3.5 text-xs sm:text-sm text-slate-300 leading-relaxed font-sans">
              <p>
                Si a todos los árboles les entregamos la misma tabla de datos, todos aprenderían exactamente lo mismo. Para evitarlo aplicamos <strong class="text-white">Bagging</strong>:
              </p>

              <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-2">
                <span class="text-xs font-mono text-emerald-300 font-bold block">&bull; Sorteo con Reemplazo (Bootstrap):</span>
                <p class="text-xs text-slate-300">
                  A cada árbol se le entrega un paquete de datos distinto mediante un sorteo con reemplazo. Es como sacar un dato de la bolsa, anotarlo y volverlo a meter.
                </p>
                <p class="text-xs text-slate-300">
                  Como consecuencia, <strong class="text-cyan-300">algunos datos se le repiten</strong> a un mismo árbol, y otros quedan fuera.
                </p>
              </div>

              <div class="p-3.5 rounded-xl bg-cyan-950/30 border border-cyan-500/30 space-y-1.5">
                <span class="text-xs font-mono text-cyan-300 font-bold block">&bull; El 37% de Datos Out-of-Bag (OOB):</span>
                <p class="text-xs text-slate-300">
                  Aproximadamente el <strong class="text-white font-mono">&approx; 37% de los datos NUNCA los ve ese árbol específico</strong>.
                </p>
                <p class="text-[11px] text-slate-400">
                  Estos datos no vistos se llaman <em>Out-of-Bag</em> y sirven para evaluar qué tan bien funciona el modelo en la práctica, sin necesidad de separar exámenes adicionales o validaciones costosas.
                </p>
              </div>
            </div>
          </div>

          <!-- Direct Illustration Card -->
          <div class="lg:col-span-5 example-card p-5 rounded-2xl space-y-4">
            <h3 class="text-xs font-mono text-cyan-400 uppercase tracking-wider font-bold flex items-center gap-2">
              <i data-lucide="pie-chart" class="w-4 h-4 text-cyan-400"></i>
              Composición de Datos por Árbol
            </h3>

            <!-- Visual Bar -->
            <div class="space-y-2">
              <div class="flex justify-between text-xs font-mono">
                <span class="text-emerald-400 font-bold">Datos Vistos (~63%)</span>
                <span class="text-rose-400 font-bold">Out-of-Bag (~37%)</span>
              </div>
              <div class="w-full h-4 bg-slate-800 rounded-full overflow-hidden flex">
                <div class="bg-emerald-500 h-full w-[63%]" title="En-Bolsa (Bootstrap)"></div>
                <div class="bg-rose-500 h-full w-[37%]" title="Out-of-Bag (Validación)"></div>
              </div>
              <div class="flex justify-between text-[10px] font-mono text-slate-400">
                <span>Entrenamiento con repetición</span>
                <span>Examen honesto no visto</span>
              </div>
            </div>

            <!-- Bullet Summary -->
            <div class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs space-y-1.5 font-sans">
              <span class="text-xs font-mono text-slate-200 font-bold block">Ventajas de Bagging:</span>
              <ul class="space-y-1 text-slate-300 text-[11px]">
                <li>&check; Crea universos paralelos de entrenamiento.</li>
                <li>&check; Cada árbol tiene su propia perspectiva del dataset.</li>
                <li>&check; Validación OOB inmediata y gratuita.</li>
              </ul>
            </div>

            <!-- Takeaway Card -->
            <div class="takeaway-card p-3 rounded-xl space-y-1">
              <span class="text-[10px] font-mono uppercase tracking-wider text-amber-400 font-bold block">💡 Conclusión Clave:</span>
              <p class="text-[11px] text-amber-200 leading-snug">
                El remuestreo con reemplazo asegura que cada árbol experimente una versión única de la realidad, dejando un 37% de reserva para auditoría.
              </p>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- ==================================================================== -->
    <!-- SLIDE 6: 3C. PILAR 3: SUBESPACIO DE CARACTERÍSTICAS                  -->
    <!-- ==================================================================== -->
    <section id="slide-6" class="slide-section py-4">
      <div class="space-y-4">
        <!-- Title -->
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-2 border-b border-slate-800 pb-3">
          <div>
            <div class="text-xs font-mono text-cyan-400 uppercase tracking-wider font-semibold">3. ¿Cómo Funciona? &bull; Segundo Nivel de Aleatoriedad</div>
            <h2 class="text-2xl md:text-3xl font-extrabold text-white">
              Pilar C: Subespacio de Características
            </h2>
          </div>
          <div class="text-xs font-mono text-cyan-300 bg-cyan-950 px-3 py-1.5 rounded-lg border border-cyan-500/40">
            Muestreo de Columnas &bull; Ruptura del Monopolio
          </div>
        </div>

        <!-- Slide Objective Banner -->
        <div class="objective-card p-3.5 rounded-xl flex items-start gap-3">
          <div class="w-8 h-8 rounded-lg bg-emerald-500/20 border border-emerald-500/40 flex items-center justify-center text-emerald-400 shrink-0 mt-0.5">
            <i data-lucide="target" class="w-4 h-4 text-emerald-400"></i>
          </div>
          <div>
            <span class="text-[11px] font-mono uppercase tracking-wider text-emerald-400 font-bold block">🎯 Objetivo de la Diapositiva:</span>
            <p class="text-xs sm:text-sm text-slate-200 leading-relaxed font-sans">
              Entender por qué Bagging por sí solo no basta cuando hay variables dominantes, y cómo forzar a los árboles a elegir entre subconjuntos reducidos de variables garantiza la independencia.
            </p>
          </div>
        </div>

        <!-- Main Content Grid -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          
          <!-- Theory Card -->
          <div class="lg:col-span-7 theory-card p-5 rounded-2xl space-y-4">
            <h3 class="text-xs font-mono text-cyan-400 uppercase tracking-wider font-bold flex items-center gap-2">
              <i data-lucide="columns" class="w-4 h-4 text-cyan-400"></i>
              El Problema del Monopolio de Variables
            </h3>

            <div class="space-y-3.5 text-xs sm:text-sm text-slate-300 leading-relaxed font-sans">
              <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-1.5">
                <strong class="text-white block font-mono text-xs">&bull; ¿Qué pasa si hay una variable demasiado evidente?</strong>
                <p class="text-slate-300 text-xs">
                  Si hay una variable hiperpredictiva, <strong>todos los árboles querrán mirarla primero en la raíz</strong>. Aunque los datos tengan Bagging, todos los árboles empezarían con la misma pregunta y terminarían pareciéndose demasiado.
                </p>
              </div>

              <div class="p-3.5 rounded-xl bg-cyan-950/30 border border-cyan-500/30 space-y-2">
                <strong class="text-cyan-300 block font-mono text-xs">&bull; La Solución: Ocultar Variables Deliberadamente:</strong>
                <p class="text-xs text-slate-300">
                  En cada bifurcación o pregunta que hace el árbol, el algoritmo <strong>le esconde deliberadamente algunas variables</strong> y lo obliga a elegir entre un subgrupo pequeño al azar (por ejemplo, solo 2 de 4 variables disponibles).
                </p>
                <div class="p-2.5 rounded bg-slate-950 border border-slate-800 text-[11px] font-mono text-emerald-400">
                  Efecto: Unos árboles aprenden con unas variables, y otros descubren rutas alternativas complementarias.
                </div>
              </div>
            </div>
          </div>

          <!-- Direct Illustration Card -->
          <div class="lg:col-span-5 example-card p-5 rounded-2xl space-y-4">
            <h3 class="text-xs font-mono text-emerald-400 uppercase tracking-wider font-bold flex items-center gap-2">
              <i data-lucide="shuffle" class="w-4 h-4 text-emerald-400"></i>
              Ejemplo Visual de Subespacio
            </h3>

            <div class="space-y-2 text-xs font-mono">
              <span class="text-slate-400 text-[11px] block">Dataset con 4 variables disponibles:</span>
              <div class="grid grid-cols-2 gap-2">
                <div class="p-2 rounded bg-cyan-950/60 border border-cyan-500/50 text-cyan-300 text-center font-bold">
                  ✓ Tamaño
                </div>
                <div class="p-2 rounded bg-slate-900 border border-slate-800 text-slate-600 text-center line-through">
                  ✗ Forma (Oculta)
                </div>
                <div class="p-2 rounded bg-slate-900 border border-slate-800 text-slate-600 text-center line-through">
                  ✗ Color (Oculto)
                </div>
                <div class="p-2 rounded bg-cyan-950/60 border border-cyan-500/50 text-cyan-300 text-center font-bold">
                  ✓ Contenido
                </div>
              </div>
              <p class="text-[11px] text-slate-400 pt-1 leading-snug font-sans">
                En este nodo, el árbol solo puede elegir entre <strong>Tamaño</strong> y <strong>Contenido</strong>. El monopolio de la "Forma" queda roto.
              </p>
            </div>

            <!-- Takeaway Card -->
            <div class="takeaway-card p-3 rounded-xl space-y-1">
              <span class="text-[10px] font-mono uppercase tracking-wider text-amber-400 font-bold block">💡 Conclusión Clave:</span>
              <p class="text-[11px] text-amber-200 leading-snug">
                La ceguera parcial impuesta a los nodos no debilita al modelo: lo hace invencible al forzar la diversidad de perspectivas.
              </p>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- ==================================================================== -->
    <!-- SLIDE 7: 4. EJEMPLO PRÁCTICO: SEÑALES DE CRUCE PEATONAL             -->
    <!-- ==================================================================== -->
    <section id="slide-7" class="slide-section py-4">
      <div class="space-y-4">
        <!-- Title -->
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-2 border-b border-slate-800 pb-3">
          <div>
            <div class="text-xs font-mono text-emerald-400 uppercase tracking-wider font-semibold">4. El Ejemplo Práctico &bull; Aplicación Directa</div>
            <h2 class="text-2xl md:text-3xl font-extrabold text-white">
              Clasificación de Señales de Cruce Peatonal
            </h2>
          </div>
          <div class="text-xs font-mono text-emerald-300 bg-emerald-950 px-3 py-1.5 rounded-lg border border-emerald-500/40">
            Árbol Solitario vs. Bosque
          </div>
        </div>

        <!-- Slide Objective Banner -->
        <div class="objective-card p-3.5 rounded-xl flex items-start gap-3">
          <div class="w-8 h-8 rounded-lg bg-emerald-500/20 border border-emerald-500/40 flex items-center justify-center text-emerald-400 shrink-0 mt-0.5">
            <i data-lucide="target" class="w-4 h-4 text-emerald-400"></i>
          </div>
          <div>
            <span class="text-[11px] font-mono uppercase tracking-wider text-emerald-400 font-bold block">🎯 Objetivo de la Diapositiva:</span>
            <p class="text-xs sm:text-sm text-slate-200 leading-relaxed font-sans">
              Ver con un caso concreto de 4 variables cómo la votación mayoritaria del bosque rescata una predicción correcta cuando un árbol rígido solitario se equivoca.
            </p>
          </div>
        </div>

        <!-- Main Content Grid -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          
          <!-- Problem Setup Card -->
          <div class="lg:col-span-6 theory-card p-5 rounded-2xl space-y-4">
            <h3 class="text-xs font-mono text-emerald-400 uppercase tracking-wider font-bold flex items-center gap-2">
              <i data-lucide="map-pin" class="w-4 h-4 text-emerald-400"></i>
              El Escenario: Clasificar si es Cruce Peatonal (Sí / No)
            </h3>

            <div class="space-y-3 text-xs sm:text-sm text-slate-300 leading-relaxed font-sans">
              <p>
                Evaluamos cuatro características de cada señal vial:
              </p>
              <div class="grid grid-cols-2 gap-2 text-xs font-mono">
                <div class="p-2 rounded bg-slate-900 border border-slate-800">
                  <span class="text-cyan-300 font-bold block">1. Tamaño:</span>
                  Pequeño, Mediano o Grande.
                </div>
                <div class="p-2 rounded bg-slate-900 border border-slate-800">
                  <span class="text-cyan-300 font-bold block">2. Forma / Lados:</span>
                  3, 4, 8 lados o Círculo.
                </div>
                <div class="p-2 rounded bg-slate-900 border border-slate-800">
                  <span class="text-cyan-300 font-bold block">3. Colores:</span>
                  Unicolor, Bicolor o Multicolor.
                </div>
                <div class="p-2 rounded bg-slate-900 border border-slate-800">
                  <span class="text-cyan-300 font-bold block">4. Contenido:</span>
                  Texto escrito o Símbolo gráfico.
                </div>
              </div>

              <!-- Single tree failure -->
              <div class="p-3.5 rounded-xl bg-rose-950/20 border border-rose-500/40 text-xs space-y-1">
                <strong class="text-rose-400 font-mono block">&bull; Fallo del Árbol Solitario:</strong>
                <p class="text-slate-200">
                  Podría aprender una regla rígida memorizada como: <em>"Si la señal es redonda, jamás es un cruce"</em>. Ante una señal circular europea especial con peatón, se equivoca rotundamente diciendo que <strong>NO</strong>.
                </p>
              </div>
            </div>
          </div>

          <!-- Forest Success Card -->
          <div class="lg:col-span-6 example-card p-5 rounded-2xl space-y-4">
            <h3 class="text-xs font-mono text-cyan-400 uppercase tracking-wider font-bold flex items-center gap-2">
              <i data-lucide="check-check" class="w-4 h-4 text-cyan-400"></i>
              Éxito del Bosque por Voto Mayoritario
            </h3>

            <div class="space-y-2 text-xs font-mono">
              <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 flex justify-between items-center">
                <span>&bull; Árbol 1 (mira forma circular):</span>
                <span class="text-rose-400 font-bold">Dice "NO" (Falla)</span>
              </div>
              <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 flex justify-between items-center">
                <span>&bull; Árbol 2 (mira color y símbolo peatón):</span>
                <span class="text-emerald-400 font-bold">Dice "SÍ" (Acierta)</span>
              </div>
              <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 flex justify-between items-center">
                <span>&bull; Árbol 3 (mira tamaño y contexto):</span>
                <span class="text-emerald-400 font-bold">Dice "SÍ" (Acierta)</span>
              </div>
            </div>

            <!-- Majority Result Box -->
            <div class="p-4 rounded-xl bg-emerald-950/40 border border-emerald-500/50 flex items-center justify-between">
              <div>
                <span class="text-[10px] font-mono uppercase text-emerald-400 font-bold block">Votación Mayoritaria (2 vs 1):</span>
                <span class="text-lg font-bold font-mono text-white">Predicción Final: SÍ (CRUCE)</span>
              </div>
              <div class="w-10 h-10 rounded-full bg-emerald-500 text-slate-950 flex items-center justify-center font-bold text-lg">
                ✓
              </div>
            </div>

            <!-- Takeaway Card -->
            <div class="takeaway-card p-3 rounded-xl space-y-1">
              <span class="text-[10px] font-mono uppercase tracking-wider text-amber-400 font-bold block">💡 Conclusión Clave:</span>
              <p class="text-[11px] text-amber-200 leading-snug">
                El árbol solitario se bloqueó por una regla dogmática; el bosque razonó holísticamente combinando múltiples perspectivas para salvar la predicción.
              </p>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- ==================================================================== -->
    <!-- SLIDE 8: 5A. CRITERIO TÉCNICO: INTERPRETABILIDAD CON SHAP            -->
    <!-- ==================================================================== -->
    <section id="slide-8" class="slide-section py-4">
      <div class="space-y-4">
        <!-- Title -->
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-2 border-b border-slate-800 pb-3">
          <div>
            <div class="text-xs font-mono text-rose-400 uppercase tracking-wider font-semibold">5. Criterio Técnico y Puntos Críticos &bull; Explicabilidad / XAI</div>
            <h2 class="text-2xl md:text-3xl font-extrabold text-white">
              A. Interpretabilidad Real con SHAP
            </h2>
          </div>
          <div class="text-xs font-mono text-cyan-300 bg-cyan-950 px-3 py-1.5 rounded-lg border border-cyan-500/40">
            Valores de Shapley &bull; Superando a Gini
          </div>
        </div>

        <!-- Slide Objective Banner -->
        <div class="objective-card p-3.5 rounded-xl flex items-start gap-3">
          <div class="w-8 h-8 rounded-lg bg-emerald-500/20 border border-emerald-500/40 flex items-center justify-center text-emerald-400 shrink-0 mt-0.5">
            <i data-lucide="target" class="w-4 h-4 text-emerald-400"></i>
          </div>
          <div>
            <span class="text-[11px] font-mono uppercase tracking-wider text-emerald-400 font-bold block">🎯 Objetivo de la Diapositiva:</span>
            <p class="text-xs sm:text-sm text-slate-200 leading-relaxed font-sans">
              Identificar la debilidad de la métrica tradicional de Gini (carece de dirección) y entender cómo los valores de Shapley (SHAP) permiten auditar con exactitud decisiones de misión crítica.
            </p>
          </div>
        </div>

        <!-- Main Content Grid -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          
          <!-- Theory Card -->
          <div class="lg:col-span-7 theory-card p-5 rounded-2xl space-y-4">
            <h3 class="text-xs font-mono text-rose-400 uppercase tracking-wider font-bold flex items-center gap-2">
              <i data-lucide="eye" class="w-4 h-4 text-rose-400"></i>
              Más Allá de la Caja Negra: ¿Por qué Decidió el Bosque?
            </h3>

            <div class="space-y-3.5 text-xs sm:text-sm text-slate-300 leading-relaxed font-sans">
              <div class="p-3.5 rounded-xl bg-slate-900 border border-rose-500/30 space-y-1.5">
                <strong class="text-rose-400 block font-mono text-xs">&bull; El Límite de la Métrica Clásica (Gini):</strong>
                <p class="text-xs text-slate-300">
                  La métrica clásica de importancia de variables (<em>Gini</em>) solo dice <strong>cuánto importa una variable</strong> en bruto, pero no aclara si esa variable empuja la predicción hacia un resultado positivo o negativo.
                </p>
              </div>

              <div class="p-3.5 rounded-xl bg-emerald-950/20 border border-emerald-500/30 space-y-2">
                <strong class="text-emerald-400 block font-mono text-xs">&bull; Herramientas Modernas como SHAP (Teoría de Juegos):</strong>
                <p class="text-xs text-slate-300">
                  Herramientas modernas como <strong class="text-white">SHAP</strong> (basadas en la teoría de juegos del Premio Nobel Lloyd Shapley) permiten auditar el modelo para ver con exactitud <strong>qué valores específicos hacen que el bosque tome una decisión médica, financiera o de clasificación</strong>.
                </p>
              </div>
            </div>
          </div>

          <!-- Direct Comparison Card -->
          <div class="lg:col-span-5 example-card p-5 rounded-2xl space-y-4">
            <h3 class="text-xs font-mono text-cyan-400 uppercase tracking-wider font-bold flex items-center gap-2">
              <i data-lucide="git-compare" class="w-4 h-4 text-cyan-400"></i>
              Comparativa Directa de Auditoría
            </h3>

            <div class="space-y-2.5 text-xs font-mono">
              <div class="p-3 rounded-xl bg-slate-900 border border-rose-500/30 space-y-1">
                <span class="text-rose-400 font-bold block">Gini Clásico:</span>
                <p class="text-slate-400 text-[11px] font-sans">
                  "La variable Glucosa tuvo una importancia de 0.42".<br>
                  <span class="text-rose-300 font-mono text-[10px]">&rarr; ¿Tener más glucosa aumentó o bajó el riesgo? Gini no lo sabe.</span>
                </p>
              </div>

              <div class="p-3 rounded-xl bg-slate-900 border border-emerald-500/40 space-y-1">
                <span class="text-emerald-400 font-bold block">Valores SHAP:</span>
                <p class="text-slate-300 text-[11px] font-sans">
                  "Glucosa = 145 mg/dL sumó +18% al riesgo de diabetes en este paciente".<br>
                  <span class="text-emerald-300 font-mono text-[10px]">&rarr; Tiene magnitud y dirección (+ / -) por paciente.</span>
                </p>
              </div>
            </div>

            <!-- Takeaway Card -->
            <div class="takeaway-card p-3 rounded-xl space-y-1">
              <span class="text-[10px] font-mono uppercase tracking-wider text-amber-400 font-bold block">💡 Conclusión Clave:</span>
              <p class="text-[11px] text-amber-200 leading-snug">
                Gini te dice cuánto se usó una variable; SHAP te explica por qué el paciente fue diagnosticado con exactitud y rigor ético.
              </p>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- ==================================================================== -->
    <!-- SLIDE 9: 5B. CRITERIO TÉCNICO: LÍMITE DE EXTRAPOLACIÓN               -->
    <!-- ==================================================================== -->
    <section id="slide-9" class="slide-section py-4">
      <div class="space-y-4">
        <!-- Title -->
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-2 border-b border-slate-800 pb-3">
          <div>
            <div class="text-xs font-mono text-rose-400 uppercase tracking-wider font-semibold">5. Criterio Técnico y Puntos Críticos &bull; Límite Matemático</div>
            <h2 class="text-2xl md:text-3xl font-extrabold text-white">
              B. Incapacidad de Extrapolación
            </h2>
          </div>
          <div class="text-xs font-mono text-rose-300 bg-rose-950 px-3 py-1.5 rounded-lg border border-rose-500/40">
            Aplanamiento Horizontal en Series de Tiempo
          </div>
        </div>

        <!-- Slide Objective Banner -->
        <div class="objective-card p-3.5 rounded-xl flex items-start gap-3">
          <div class="w-8 h-8 rounded-lg bg-emerald-500/20 border border-emerald-500/40 flex items-center justify-center text-emerald-400 shrink-0 mt-0.5">
            <i data-lucide="target" class="w-4 h-4 text-emerald-400"></i>
          </div>
          <div>
            <span class="text-[11px] font-mono uppercase tracking-wider text-emerald-400 font-bold block">🎯 Objetivo de la Diapositiva:</span>
            <p class="text-xs sm:text-sm text-slate-200 leading-relaxed font-sans">
              Comprender por qué los modelos basados en árboles no pueden extrapolar tendencias crecientes en series temporales y deducir la regla de oro: nunca predecir valores superiores a los históricos.
            </p>
          </div>
        </div>

        <!-- Main Content Grid -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          
          <!-- Theory Card -->
          <div class="lg:col-span-7 theory-card p-5 rounded-2xl space-y-4">
            <h3 class="text-xs font-mono text-rose-400 uppercase tracking-wider font-bold flex items-center gap-2">
              <i data-lucide="trending-up" class="w-4 h-4 text-rose-400"></i>
              La Geometría de los Árboles y su Techo Infranqueable
            </h3>

            <div class="space-y-3.5 text-xs sm:text-sm text-slate-300 leading-relaxed font-sans">
              <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-1.5">
                <strong class="text-white block font-mono text-xs">&bull; Los árboles no dibujan líneas continuas:</strong>
                <p class="text-xs text-slate-300">
                  Los árboles no proyectan líneas hacia el infinito; dividen el espacio en <strong class="text-cyan-300">"cajas" (hiperrectángulos)</strong> y calculan el promedio aritmético de lo que cayó adentro durante el entrenamiento.
                </p>
              </div>

              <div class="p-3.5 rounded-xl bg-rose-950/20 border border-rose-500/40 space-y-2">
                <strong class="text-rose-400 block font-mono text-xs">&bull; El Límite Matemático Estricto:</strong>
                <p class="text-xs text-slate-200 font-bold">
                  Random Forest no puede predecir valores mayores a los máximos que ya vio en el entrenamiento.
                </p>
                <p class="text-xs text-slate-300">
                  Si se usa para predecir series temporales con tendencia al alza (como proyecciones de ventas o inflación futura), <strong class="text-rose-300">el modelo simplemente se aplana en una línea horizontal constante</strong>.
                </p>
              </div>
            </div>
          </div>

          <!-- Direct Illustration Card -->
          <div class="lg:col-span-5 example-card p-5 rounded-2xl space-y-4">
            <h3 class="text-xs font-mono text-cyan-400 uppercase tracking-wider font-bold flex items-center gap-2">
              <i data-lucide="bar-chart-2" class="w-4 h-4 text-cyan-400"></i>
              Demostración Visual del Aplanamiento
            </h3>

            <!-- SVG Visual -->
            <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 flex flex-col items-center">
              <svg viewBox="0 0 240 120" class="w-full h-32">
                <!-- Axes -->
                <line x1="20" y1="100" x2="220" y2="100" stroke="#475569" stroke-width="1.5"/>
                <line x1="20" y1="10" x2="20" y2="100" stroke="#475569" stroke-width="1.5"/>
                
                <!-- History boundary line -->
                <line x1="120" y1="10" x2="120" y2="100" stroke="#64748b" stroke-dasharray="3,3" stroke-width="1.5"/>
                <text x="70" y="20" font-size="8" font-family="monospace" fill="#94a3b8" text-anchor="middle">Histórico (Train)</text>
                <text x="170" y="20" font-size="8" font-family="monospace" fill="#f43f5e" text-anchor="middle">Futuro (Tendencia)</text>
                
                <!-- Real Trend Line (Linear) -->
                <line x1="20" y1="90" x2="220" y2="25" stroke="#38bdf8" stroke-width="2" stroke-dasharray="2,2"/>
                
                <!-- Random Forest Flat Line -->
                <path d="M20,90 L60,75 L90,60 L120,50 L220,50" fill="none" stroke="#fb7185" stroke-width="3"/>
                <circle cx="120" cy="50" r="3" fill="#fb7185"/>
                <text x="175" y="44" font-size="7.5" font-family="monospace" fill="#fb7185" font-weight="bold" text-anchor="middle">Techo Horizontal</text>
              </svg>
              <div class="flex justify-between w-full text-[10px] font-mono text-slate-400 pt-1 border-t border-slate-800">
                <span class="text-cyan-400">&bull; Tendencia Real (Continúa)</span>
                <span class="text-rose-400">&bull; Random Forest (Aplanado)</span>
              </div>
            </div>

            <!-- Takeaway Card -->
            <div class="takeaway-card p-3 rounded-xl space-y-1">
              <span class="text-[10px] font-mono uppercase tracking-wider text-amber-400 font-bold block">💡 Conclusión Clave:</span>
              <p class="text-[11px] text-amber-200 leading-snug">
                Random Forest es un maestro de la interpolación local, pero está ciego ante la extrapolación. Para series con tendencia, primero debes diferenciar los datos.
              </p>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- ==================================================================== -->
    <!-- SLIDE 10: 5C. CRITERIO TÉCNICO: HARDWARE & DESPLIEGUE EN ONNX        -->
    <!-- ==================================================================== -->
    <section id="slide-10" class="slide-section py-4">
      <div class="space-y-4">
        <!-- Title -->
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-2 border-b border-slate-800 pb-3">
          <div>
            <div class="text-xs font-mono text-amber-400 uppercase tracking-wider font-semibold">5. Criterio Técnico y Puntos Críticos &bull; Producción e Ingeniería</div>
            <h2 class="text-2xl md:text-3xl font-extrabold text-white">
              C. Eficiencia de Hardware e Implementación
            </h2>
          </div>
          <div class="text-xs font-mono text-amber-300 bg-amber-950 px-3 py-1.5 rounded-lg border border-amber-500/40">
            Paralelismo CPU &bull; Despliegue en C# / Go (.ONNX)
          </div>
        </div>

        <!-- Slide Objective Banner -->
        <div class="objective-card p-3.5 rounded-xl flex items-start gap-3">
          <div class="w-8 h-8 rounded-lg bg-emerald-500/20 border border-emerald-500/40 flex items-center justify-center text-emerald-400 shrink-0 mt-0.5">
            <i data-lucide="target" class="w-4 h-4 text-emerald-400"></i>
          </div>
          <div>
            <span class="text-[11px] font-mono uppercase tracking-wider text-emerald-400 font-bold block">🎯 Objetivo de la Diapositiva:</span>
            <p class="text-xs sm:text-sm text-slate-200 leading-relaxed font-sans">
              Analizar cómo la independencia de los árboles permite entrenar y evaluar en paralelo en todos los núcleos de CPU, y cómo el estándar ONNX permite servir modelos a gran velocidad sin depender de Python.
            </p>
          </div>
        </div>

        <!-- Main Content Grid -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          
          <!-- Theory Card -->
          <div class="lg:col-span-7 theory-card p-5 rounded-2xl space-y-4">
            <h3 class="text-xs font-mono text-amber-400 uppercase tracking-wider font-bold flex items-center gap-2">
              <i data-lucide="cpu" class="w-4 h-4 text-amber-400"></i>
              Arquitectura de Cómputo e Inferencia
            </h3>

            <div class="space-y-3.5 text-xs sm:text-sm text-slate-300 leading-relaxed font-sans">
              <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-1.5">
                <strong class="text-white block font-mono text-xs">&bull; Paralelismo Masivo en CPU:</strong>
                <p class="text-xs text-slate-300">
                  A diferencia de otros modelos secuenciales (como Gradient Boosting, donde cada árbol espera al anterior), los cientos de árboles de Random Forest son <strong class="text-emerald-400 font-bold">totalmente independientes</strong>.
                </p>
                <p class="text-xs text-slate-400">
                  Se pueden entrenar y evaluar en paralelo repartiendo el trabajo de forma simultánea entre todos los núcleos de un procesador (<strong>CPU</strong>).
                </p>
              </div>

              <div class="p-3.5 rounded-xl bg-cyan-950/30 border border-cyan-500/30 space-y-1.5">
                <strong class="text-cyan-300 block font-mono text-xs">&bull; Despliegue en Producción sin Python (ONNX):</strong>
                <p class="text-xs text-slate-300">
                  Para producción real, el modelo se exporta a formatos estándar como <strong class="text-white font-mono">ONNX</strong>.
                </p>
                <p class="text-xs text-slate-300">
                  Esto permite que un microservicio en <strong class="text-cyan-300">C# (.NET) o Go</strong> lo ejecute a gran velocidad en milisegundos, sin depender del intérprete pesado de Python ni de sus bloqueos de memoria (GIL).
                </p>
              </div>
            </div>
          </div>

          <!-- Direct Illustration Card -->
          <div class="lg:col-span-5 example-card p-5 rounded-2xl space-y-4">
            <h3 class="text-xs font-mono text-emerald-400 uppercase tracking-wider font-bold flex items-center gap-2">
              <i data-lucide="server" class="w-4 h-4 text-emerald-400"></i>
              Pipeline de Producción Desacoplado
            </h3>

            <!-- 3 step pipeline -->
            <div class="space-y-2 text-xs font-mono">
              <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 flex items-center gap-2">
                <span class="w-5 h-5 rounded-full bg-slate-800 text-slate-300 flex items-center justify-center text-[10px] font-bold">1</span>
                <div>
                  <span class="text-slate-200 font-bold block">Entrenamiento Offline</span>
                  <span class="text-[10px] text-slate-400 font-sans">Python / Scikit-Learn en CPU multinúcleo</span>
                </div>
              </div>
              <div class="p-2.5 rounded-lg bg-cyan-950/40 border border-cyan-500/30 flex items-center gap-2">
                <span class="w-5 h-5 rounded-full bg-cyan-900 text-cyan-300 flex items-center justify-center text-[10px] font-bold">2</span>
                <div>
                  <span class="text-cyan-300 font-bold block">Exportación a ONNX</span>
                  <span class="text-[10px] text-slate-400 font-sans">Binario agnóstico y ultraliviano (.onnx)</span>
                </div>
              </div>
              <div class="p-2.5 rounded-lg bg-emerald-950/40 border border-emerald-500/30 flex items-center gap-2">
                <span class="w-5 h-5 rounded-full bg-emerald-900 text-emerald-300 flex items-center justify-center text-[10px] font-bold">3</span>
                <div>
                  <span class="text-emerald-300 font-bold block">Servicio en C# (.NET) / Go</span>
                  <span class="text-[10px] text-slate-400 font-sans">Inferencia sub-milisegundo sin Python</span>
                </div>
              </div>
            </div>

            <!-- Takeaway Card -->
            <div class="takeaway-card p-3 rounded-xl space-y-1">
              <span class="text-[10px] font-mono uppercase tracking-wider text-amber-400 font-bold block">💡 Conclusión Clave:</span>
              <p class="text-[11px] text-amber-200 leading-snug">
                Random Forest es perfecto para la ingeniería moderna: aprovecha cada hilo de CPU al máximo y se sirve como binario nativo en la nube.
              </p>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- ==================================================================== -->
    <!-- SLIDE 11: 6. RESUMEN DE DECISIÓN (CUÁNDO SÍ VS CUÁNDO NO)            -->
    <!-- ==================================================================== -->
    <section id="slide-11" class="slide-section py-4">
      <div class="space-y-4">
        <!-- Title -->
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-2 border-b border-slate-800 pb-3">
          <div>
            <div class="text-xs font-mono text-emerald-400 uppercase tracking-wider font-semibold">6. Criterio de Selección &bull; Resumen de Decisión</div>
            <h2 class="text-2xl md:text-3xl font-extrabold text-white">
              Cuándo SÍ usar Random Forest vs. Cuándo NO
            </h2>
          </div>
          <div class="text-xs font-mono text-slate-300 bg-slate-900 px-3 py-1.5 rounded-lg border border-slate-800">
            Matriz de Decisión Definitiva
          </div>
        </div>

        <!-- Slide Objective Banner -->
        <div class="objective-card p-3.5 rounded-xl flex items-start gap-3">
          <div class="w-8 h-8 rounded-lg bg-emerald-500/20 border border-emerald-500/40 flex items-center justify-center text-emerald-400 shrink-0 mt-0.5">
            <i data-lucide="target" class="w-4 h-4 text-emerald-400"></i>
          </div>
          <div>
            <span class="text-[11px] font-mono uppercase tracking-wider text-emerald-400 font-bold block">🎯 Objetivo de la Diapositiva:</span>
            <p class="text-xs sm:text-sm text-slate-200 leading-relaxed font-sans">
              Consolidar el criterio práctico para discernir con rapidez en qué proyectos Random Forest es la mejor opción técnica y en cuáles debe descartarse en favor de otros modelos.
            </p>
          </div>
        </div>

        <!-- Two Symmetric Panels (Exact User Table) -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 items-stretch">
          
          <!-- LEFT PANEL: CUÁNDO SÍ -->
          <div class="glass-card p-6 rounded-2xl border border-emerald-500/40 bg-emerald-950/10 space-y-4 flex flex-col justify-between">
            <div class="space-y-4">
              <div class="flex items-center gap-2 border-b border-emerald-500/30 pb-3">
                <div class="w-7 h-7 rounded-lg bg-emerald-950 border border-emerald-500/40 flex items-center justify-center text-emerald-400">
                  <i data-lucide="check-circle-2" class="w-4 h-4"></i>
                </div>
                <h3 class="text-base font-bold font-mono text-emerald-400 uppercase tracking-wide">
                  Cuándo SÍ usar Random Forest
                </h3>
              </div>

              <ul class="space-y-4 text-xs sm:text-sm text-slate-200 leading-relaxed font-sans">
                <li class="flex items-start gap-3">
                  <span class="w-2 h-2 rounded-full bg-emerald-400 mt-1.5 shrink-0"></span>
                  <div>
                    <strong class="text-white block font-mono text-xs">Datos en tablas con relaciones complejas y no lineales:</strong>
                    Excelente desempeño con variables numéricas y categóricas sin necesidad de supuestos lineales.
                  </div>
                </li>

                <li class="flex items-start gap-3">
                  <span class="w-2 h-2 rounded-full bg-emerald-400 mt-1.5 shrink-0"></span>
                  <div>
                    <strong class="text-white block font-mono text-xs">Sin preprocesamiento de escala:</strong>
                    Cuando no quieres perder tiempo normalizando, estandarizando o escalando datos numéricos.
                  </div>
                </li>

                <li class="flex items-start gap-3">
                  <span class="w-2 h-2 rounded-full bg-emerald-400 mt-1.5 shrink-0"></span>
                  <div>
                    <strong class="text-white block font-mono text-xs">Modelo base confiable y robusto:</strong>
                    Cuando necesitas un modelo base muy confiable y altamente resistente al sobreajuste (*overfitting*).
                  </div>
                </li>
              </ul>
            </div>

            <div class="p-3 rounded-xl bg-emerald-950/40 border border-emerald-500/30 text-xs font-mono text-emerald-300">
              Veredicto: El estándar de oro y punto de partida obligatorio en datos tabulares.
            </div>
          </div>

          <!-- RIGHT PANEL: CUÁNDO NO -->
          <div class="glass-card p-6 rounded-2xl border border-rose-500/40 bg-rose-950/10 space-y-4 flex flex-col justify-between">
            <div class="space-y-4">
              <div class="flex items-center gap-2 border-b border-rose-500/30 pb-3">
                <div class="w-7 h-7 rounded-lg bg-rose-950 border border-rose-500/40 flex items-center justify-center text-rose-400">
                  <i data-lucide="x-circle" class="w-4 h-4"></i>
                </div>
                <h3 class="text-base font-bold font-mono text-rose-400 uppercase tracking-wide">
                  Cuándo NO usarlo
                </h3>
              </div>

              <ul class="space-y-4 text-xs sm:text-sm text-slate-200 leading-relaxed font-sans">
                <li class="flex items-start gap-3">
                  <span class="w-2 h-2 rounded-full bg-rose-400 mt-1.5 shrink-0"></span>
                  <div>
                    <strong class="text-white block font-mono text-xs">Series de tiempo con tendencia a futuro:</strong>
                    Incapacidad matemática de extrapolar valores fuera del rango histórico (el modelo se aplana).
                  </div>
                </li>

                <li class="flex items-start gap-3">
                  <span class="w-2 h-2 rounded-full bg-rose-400 mt-1.5 shrink-0"></span>
                  <div>
                    <strong class="text-white block font-mono text-xs">Dispositivos con memoria RAM muy limitada:</strong>
                    Dispositivos embebidos o microcontroladores IoT donde el almacenamiento de cientos de árboles no cabe.
                  </div>
                </li>

                <li class="flex items-start gap-3">
                  <span class="w-2 h-2 rounded-full bg-rose-400 mt-1.5 shrink-0"></span>
                  <div>
                    <strong class="text-white block font-mono text-xs">Latencia estricta sub-milisegundo:</strong>
                    Sistemas de altísima frecuencia (microsegundos) donde modelos lineales o tablas precalculadas son imperativos.
                  </div>
                </li>
              </ul>
            </div>

            <div class="p-3 rounded-xl bg-rose-950/40 border border-rose-500/30 text-xs font-mono text-rose-300">
              Veredicto: Descartar ante series con tendencia o restricciones severas de memoria edge.
            </div>
          </div>

        </div>

        <!-- Takeaway Card -->
        <div class="takeaway-card p-3 rounded-xl space-y-1">
          <span class="text-[10px] font-mono uppercase tracking-wider text-amber-400 font-bold block">💡 Conclusión Clave:</span>
          <p class="text-[11px] text-amber-200 leading-snug">
            El buen ingeniero no es quien usa el modelo más complejo, sino quien sabe exactamente cuándo elegir Random Forest y cuándo descartarlo a tiempo.
          </p>
        </div>
      </div>
    </section>

    <!-- ==================================================================== -->
    <!-- SLIDE 12: CONCLUSIONES & RONDA DE PREGUNTAS                          -->
    <!-- ==================================================================== -->
    <section id="slide-12" class="slide-section py-4">
      <div class="space-y-5">
        <!-- Title -->
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-2 border-b border-slate-800 pb-3">
          <div>
            <div class="text-xs font-mono text-cyan-400 uppercase tracking-wider font-semibold">Cierre de la Exposición &bull; Síntesis Final</div>
            <h2 class="text-2xl md:text-3xl font-extrabold text-white">
              Conclusiones & Ronda de Preguntas
            </h2>
          </div>
          <button onclick="goToSlide(1)" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-mono text-slate-200 border border-slate-700 transition">
            Volver al Inicio
          </button>
        </div>

        <!-- 4 Summary Blocks -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3">
          <div class="glass-card p-4 rounded-xl border border-slate-800 space-y-2">
            <span class="text-emerald-400 font-mono font-bold text-xs block">1. PODER DEL ENSAMBLE</span>
            <p class="text-xs text-slate-300 leading-relaxed font-sans">
              Promediar muchos árboles de decisión independientes disuelve la inestabilidad y el sobreajuste del árbol solitario.
            </p>
          </div>

          <div class="glass-card p-4 rounded-xl border border-slate-800 space-y-2">
            <span class="text-cyan-400 font-mono font-bold text-xs block">2. DOBLE ALEATORIEDAD</span>
            <p class="text-xs text-slate-300 leading-relaxed font-sans">
              Bagging (sorteo de filas con 37% OOB) y Subespacio (sorteo de columnas) garantizan la diversidad de Condorcet.
            </p>
          </div>

          <div class="glass-card p-4 rounded-xl border border-slate-800 space-y-2">
            <span class="text-rose-400 font-mono font-bold text-xs block">3. LÍMITES Y ÉTICA</span>
            <p class="text-xs text-slate-300 leading-relaxed font-sans">
              SHAP permite auditar decisiones con signo y rigor. Recuerda su incapacidad matemática para extrapolar tendencias.
            </p>
          </div>

          <div class="glass-card p-4 rounded-xl border border-slate-800 space-y-2">
            <span class="text-amber-400 font-mono font-bold text-xs block">4. LISTO PARA PRODUCCIÓN</span>
            <p class="text-xs text-slate-300 leading-relaxed font-sans">
              Escala en todos los núcleos de CPU y se sirve en microsegundos con ONNX en C# o Go sin tocar Python.
            </p>
          </div>
        </div>

        <!-- Final Message & Q&A Callout -->
        <div class="p-6 rounded-2xl bg-gradient-to-r from-emerald-950/40 via-slate-900 to-cyan-950/40 border border-emerald-500/40 text-center space-y-3">
          <div class="w-12 h-12 rounded-2xl bg-emerald-500/20 border border-emerald-500/40 flex items-center justify-center text-emerald-400 mx-auto">
            <i data-lucide="help-circle" class="w-6 h-6"></i>
          </div>
          <h3 class="text-xl sm:text-2xl font-extrabold text-white">
            ¡Muchas gracias por su atención!
          </h3>
          <p class="text-xs sm:text-sm text-slate-300 max-w-xl mx-auto font-sans leading-relaxed">
            Quedo a disposición del docente, jurado y compañeros para responder dudas, profundizar en los conceptos o abrir el debate técnico.
          </p>
          <div class="pt-2">
            <span class="text-xs font-mono text-cyan-300 bg-slate-950 px-4 py-2 rounded-full border border-slate-800">
              Denshel David Mérida Quispe &bull; Machine Learning
            </span>
          </div>
        </div>
      </div>
    </section>

  </main>

  <!-- ==================================================================== -->
  <!-- BOTTOM NAVIGATION CONTROLS BAR                                       -->
  <!-- ==================================================================== -->
  <footer class="w-full fixed bottom-0 left-0 z-50 bg-slate-950/90 backdrop-blur-md border-t border-slate-800/90 px-4 md:px-8 py-3 flex items-center justify-between">
    <!-- Prev Button -->
    <div class="flex items-center gap-2">
      <button id="nav-btn-prev" onclick="prevSlide()" class="px-3.5 py-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 border border-slate-700/60 text-slate-300 hover:text-white text-xs font-mono flex items-center gap-2 transition disabled:opacity-30 disabled:cursor-not-allowed">
        <i data-lucide="arrow-left" class="w-4 h-4"></i>
        <span class="hidden sm:inline">Anterior [←]</span>
      </button>
      <button onclick="toggleSpeakerNotes()" class="px-3 py-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 border border-slate-700/60 text-cyan-300 text-xs font-mono hidden sm:flex items-center gap-1.5 transition">
        <i data-lucide="mic" class="w-3.5 h-3.5"></i>
        <span>Guión [N]</span>
      </button>
    </div>

    <!-- Center Interactive Slide Navigation Dots (12 dots) -->
    <div class="flex items-center gap-1.5 max-w-md overflow-x-auto py-1 px-2" id="nav-dots-container">
      <!-- Populated via JS -->
    </div>

    <!-- Next Button -->
    <div class="flex items-center gap-2">
      <button id="nav-btn-next" onclick="nextSlide()" class="px-4 py-1.5 rounded-lg bg-gradient-to-r from-emerald-500 to-teal-500 hover:from-emerald-400 text-slate-950 font-bold text-xs font-mono flex items-center gap-2 transition shadow-md shadow-emerald-500/20 disabled:opacity-30 disabled:cursor-not-allowed">
        <span class="hidden sm:inline">Siguiente [→ / Espacio]</span>
        <i data-lucide="arrow-right" class="w-4 h-4"></i>
      </button>
    </div>
  </footer>

  <!-- ==================================================================== -->
  <!-- KEYBOARD SHORTCUTS HELP MODAL                                        -->
  <!-- ==================================================================== -->
  <div id="modal-help" class="fixed inset-0 bg-slate-950/80 backdrop-blur-md z-50 hidden flex items-center justify-center p-4">
    <div class="glass-card max-w-md w-full p-6 rounded-2xl border border-slate-700 space-y-4 shadow-2xl">
      <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <h3 class="text-sm font-mono font-bold text-emerald-400 uppercase tracking-wider flex items-center gap-2">
          <i data-lucide="command" class="w-4 h-4"></i>
          Atajos de Teclado para la Exposición
        </h3>
        <button onclick="toggleHelpModal()" class="text-slate-400 hover:text-white p-1 rounded-lg">
          <i data-lucide="x" class="w-4 h-4"></i>
        </button>
      </div>

      <div class="space-y-2.5 text-xs font-mono">
        <div class="flex justify-between items-center py-1.5 border-b border-slate-800/60">
          <span class="text-slate-300">Avanzar Diapositiva:</span>
          <div class="flex gap-1">
            <kbd class="px-2 py-0.5 rounded bg-slate-900 border border-slate-700 text-slate-200">&rarr;</kbd>
            <kbd class="px-2 py-0.5 rounded bg-slate-900 border border-slate-700 text-slate-200">Espacio</kbd>
          </div>
        </div>
        <div class="flex justify-between items-center py-1.5 border-b border-slate-800/60">
          <span class="text-slate-300">Retroceder Diapositiva:</span>
          <kbd class="px-2 py-0.5 rounded bg-slate-900 border border-slate-700 text-slate-200">&larr;</kbd>
        </div>
        <div class="flex justify-between items-center py-1.5 border-b border-slate-800/60">
          <span class="text-slate-300">Alternar Guión / Libreto Oral:</span>
          <kbd class="px-2 py-0.5 rounded bg-slate-900 border border-slate-700 text-cyan-300 font-bold">N</kbd>
        </div>
        <div class="flex justify-between items-center py-1.5 border-b border-slate-800/60">
          <span class="text-slate-300">Pantalla Completa:</span>
          <kbd class="px-2 py-0.5 rounded bg-slate-900 border border-slate-700 text-slate-200">F</kbd>
        </div>
        <div class="flex justify-between items-center py-1.5">
          <span class="text-slate-300">Mostrar / Ocultar Ayuda:</span>
          <kbd class="px-2 py-0.5 rounded bg-slate-900 border border-slate-700 text-slate-200">?</kbd>
        </div>
      </div>

      <div class="pt-2 text-center">
        <button onclick="toggleHelpModal()" class="w-full py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-mono transition">
          Cerrar
        </button>
      </div>
    </div>
  </div>

  <!-- ==================================================================== -->
  <!-- JAVASCRIPT CONTROLLER                                                -->
  <!-- ==================================================================== -->
  <script>
    let currentSlide = 1;
    const totalSlides = 12;
    let isSpeakerNotesOpen = false;

    const SLIDE_TITLES = [
      "1. Portada & Mapa de Ruta",
      "2. 1. ¿Qué es Random Forest?",
      "3. 2. El Problema: Inestabilidad",
      "4. 3A. Sabiduría de las Masas",
      "5. 3B. Bagging y Muestreo",
      "6. 3C. Subespacio de Variables",
      "7. 4. Ejemplo: Señales Viales",
      "8. 5A. Interpretabilidad con SHAP",
      "9. 5B. Límite de Extrapolación",
      "10. 5C. Hardware y ONNX",
      "11. 6. Resumen de Decisión",
      "12. Conclusiones y Preguntas"
    ];

    const SPEAKER_NOTES = {
      1: {
        title: "Portada & Mapa de Ruta de la Exposición",
        objective: "Establecer la hoja de ruta integral de la exposición teórica y presentar al expositor.",
        script: `<p><strong>Buenos días/tardes profesor y compañeros.</strong></p>
                 <p>El día de hoy voy a presentarles los fundamentos teóricos, la mecánica interna y los criterios técnicos de decisión de uno de los algoritmos más importantes de la ciencia de datos: <strong>Random Forest (Bosques Aleatorios)</strong>.</p>
                 <p>Nuestra exposición se estructurará en 6 partes clave: primero veremos qué es y la analogía del comité; segundo, el problema de inestabilidad que viene a resolver; tercero, sus tres pilares matemáticos; cuarto, un ejemplo práctico directo con señales viales; quinto, sus límites técnicos reales en producción; y finalmente, la matriz de decisión de cuándo sí y cuándo no utilizarlo.</p>`,
        tips: "Habla con tono calmado y seguro. Destaca que la exposición prioriza la claridad conceptual antes de cualquier tecnicismo."
      },
      2: {
        title: "1. ¿Qué es Random Forest? (Contexto General)",
        objective: "Definir Random Forest dentro del aprendizaje en ensamble y explicar la analogía médica del panel de especialistas.",
        script: `<p>Comencemos por el principio: ¿qué es exactamente Random Forest?</p>
                 <p>Es un algoritmo que pertenece a la familia del <strong>aprendizaje en ensamble (ensemble learning)</strong>. Su premisa es simple pero brillante: en lugar de confiar ciegamente en lo que dice un solo modelo, reúne las predicciones de decenas o cientos de árboles de decisión individuales para emitir un veredicto conjunto por votación mayoritaria.</p>
                 <p>Pensemos en la <strong>analogía médica</strong>: si tienes una enfermedad compleja y consultas a un solo médico, corres el riesgo de que esa persona tenga un mal día o un sesgo particular. Pero si consultas a un comité de 100 especialistas independientes y decides por la mayoría de votos, el riesgo de error se desploma drásticamente. Eso es Random Forest.</p>`,
        tips: "Enfatiza la analogía médica: es el concepto que el jurado recordará de inmediato."
      },
      3: {
        title: "2. El Problema que Resuelve: La Inestabilidad del Árbol Individual",
        objective: "Explicar cómo piensa un árbol y su defecto fatal: la alta varianza y el sobreajuste (overfitting).",
        script: `<p>Para entender por qué necesitamos un bosque, primero debemos entender qué falla en un árbol solitario.</p>
                 <p>Un árbol de decisión divide los datos haciendo preguntas binarias: '¿El tumor mide más de 2 cm? ¿Tiene forma irregular?'. El problema es que los árboles profundos sufren de <strong>alta varianza y sobreajuste (overfitting)</strong>: memorizan hasta el ruido de los datos de entrenamiento.</p>
                 <p>Si cambias apenas un par de datos en el entrenamiento, la estructura de todo el árbol puede cambiar de arriba a abajo. Random Forest resuelve esto manteniendo el poder de aprendizaje del árbol, pero cancelando su inestabilidad al promediar muchos árboles.</p>`,
        tips: "Explica con las manos cómo el árbol solitario se vuelve rígido y cómo el promedio suaviza la predicción."
      },
      4: {
        title: "3. Pilar A: La Sabiduría de las Masas (Condorcet, 1785)",
        objective: "Demostrar la base matemática de la mayoría y la condición de oro de independencia.",
        script: `<p>El primer pilar teórico proviene de 1785, formulado por el matemático francés Marqués de Condorcet.</p>
                 <p>Condorcet demostró que si juntas a votantes independientes que tengan al menos una probabilidad ligeramente mayor al 50% de acertar, la probabilidad de que la mayoría del grupo acierte sube conforme sumas más miembros.</p>
                 <p>Miren la escala: 1 árbol acierta el 60%; 3 árboles suben al 65%; y 11 árboles alcanzan el 75%. Pero hay una <strong>condición de oro</strong>: los árboles deben ser diferentes entre sí. Si todos cometen el mismo error, la votación no sirve de nada.</p>`,
        tips: "Señala la escala 60% -> 65% -> 75% en pantalla para evidenciar el poder de la suma de votos."
      },
      5: {
        title: "3. Pilar B: Primer Nivel de Aleatoriedad: Bagging",
        objective: "Explicar el muestreo con reemplazo y el 37% de datos Out-of-Bag (OOB).",
        script: `<p>¿Cómo logramos que los árboles sean diferentes si solo tenemos una base de datos? Aquí entra el primer nivel de aleatoriedad: <strong>Bagging</strong>.</p>
                 <p>A cada árbol se le entrega un paquete de datos mediante un sorteo con reemplazo. Es decir, sacamos una fila al azar, la anotamos y la regresamos a la bolsa. Inevitablemente algunas filas se repetirán, y aproximadamente el <strong>37% de los datos nunca los verá ese árbol</strong>.</p>
                 <p>Esos datos no vistos se llaman <strong>Out-of-Bag (OOB)</strong> y nos regalan un examen de validación honesto y gratuito para saber cómo rinde el modelo sin gastar tiempo en pruebas adicionales.</p>`,
        tips: "Destaca el dato del 37% Out-of-Bag: es una pregunta clásica de examen en Machine Learning."
      },
      6: {
        title: "3. Pilar C: Segundo Nivel de Aleatoriedad: Subespacio de Características",
        objective: "Comprender por qué ocultar variables en cada nodo rompe el monopolio de las variables evidentes.",
        script: `<p>Bagging por sí solo no es suficiente. ¿Qué pasa si hay una variable extremadamente obvia y poderosa? Todos los árboles la elegirían en su primera pregunta y terminarían pareciéndose.</p>
                 <p>Para evitarlo, Breiman introdujo el segundo nivel de aleatoriedad: el <strong>Subespacio de Características</strong>. En cada bifurcación del árbol, el algoritmo le esconde deliberadamente algunas variables y lo obliga a elegir entre un subgrupo al azar, por ejemplo solo 2 de 4.</p>
                 <p>Al vendarle parcialmente los ojos, forzamos a que unos árboles descubran rutas alternativas que de otro modo jamás habrían sido exploradas.</p>`,
        tips: "Explica la idea de 'vendarle los ojos al árbol': ayuda mucho a fijar la intuición en la mente del público."
      },
      7: {
        title: "4. El Ejemplo Práctico: Señales de Cruce Peatonal",
        objective: "Ilustrar con el ejemplo directo de 4 características cómo el consenso 2 a 1 supera el fallo del árbol solitario.",
        script: `<p>Veamos esto en la práctica con un ejemplo muy claro: clasificar si una señal es de Cruce Peatonal evaluando 4 características: tamaño, forma, colores y contenido.</p>
                 <p>El <strong>árbol solitario</strong> aprende una regla rígida: 'Si la señal es redonda, jamás es cruce', y falla ante una señal circular europea especial.</p>
                 <p>En el <strong>bosque</strong>: el Árbol 1 mira la forma y se equivoca diciendo que NO; pero el Árbol 2 mira el símbolo peatonal y dice que SÍ; y el Árbol 3 evalúa el tamaño y dice que SÍ. Por voto de la mayoría 2 contra 1, el sistema predice correctamente SÍ. El consenso rescató la predicción.</p>`,
        tips: "Muestra la tarjeta de votación 2 a 1 en la pantalla. Es el ejemplo directo y sin rodeos que sintetiza toda la teoría previa."
      },
      8: {
        title: "5. Criterio Técnico A: Interpretabilidad con SHAP (XAI vs Gini)",
        objective: "Distinguir la importancia ciega de Gini de la explicabilidad direccional con signo de SHAP.",
        script: `<p>Pasemos a los puntos críticos de ingeniería. ¿Cómo explicamos qué decidió el bosque?</p>
                 <p>La métrica clásica de <strong>Gini</strong> solo te dice cuánto importó una variable en bruto, pero no te dice si esa variable empujó la decisión hacia positivo o negativo.</p>
                 <p>Herramientas modernas como <strong>SHAP</strong>, basadas en la teoría de juegos de Lloyd Shapley, permiten auditar exactamente con signo qué valores específicos suben o bajan el riesgo en decisiones médicas o financieras críticas. Es la diferencia entre un número ciego y una justificación ética auditable.</p>`,
        tips: "Contrasta: 'Gini es solo magnitud, SHAP tiene dirección (+/-)'."
      },
      9: {
        title: "5. Criterio Técnico B: El Límite Matemático de Extrapolación",
        objective: "Demostrar por qué los árboles se aplanan horizontalmente en series con tendencia y no pueden extrapolar.",
        script: `<p>Todo ingeniero debe saber dónde se rompe su modelo. El talón de Aquiles de Random Forest es la <strong>extrapolación en series temporales con tendencia</strong>.</p>
                 <p>Los árboles dividen el espacio en cajas y calculan el promedio histórico de lo que cayó adentro. Por eso, <strong>Random Forest jamás puede predecir un valor mayor al récord histórico que ya vio en entrenamiento</strong>.</p>
                 <p>Si intentas usarlo para predecir ventas futuras o inflación en una serie que va al alza, el modelo simplemente se aplana en una línea horizontal plana. Para series de tiempo se requiere diferenciar previamente los datos.</p>`,
        tips: "Señala la línea horizontal rosa en el gráfico de la diapositiva para que vean el techo constante."
      },
      10: {
        title: "5. Criterio Técnico C: Eficiencia de Hardware e Implementación (CPU y ONNX)",
        objective: "Explicar el paralelismo en núcleos de CPU y el desacoplamiento con ONNX en C# o Go.",
        script: `<p>En cuanto a infraestructura, Random Forest tiene una ventaja enorme: sus cientos de árboles son totalmente independientes entre sí.</p>
                 <p>Esto permite un <strong>paralelismo masivo en CPU</strong>: se pueden entrenar y evaluar distribuyendo los árboles en paralelo entre todos los núcleos del procesador sin cuellos de botella.</p>
                 <p>Y para producción a gran escala, exportamos el modelo a <strong>ONNX</strong>. Esto permite que un microservicio en <strong>C# (.NET) o Go</strong> ejecute la inferencia en milisegundos sin depender del entorno pesado de Python.</p>`,
        tips: "Menciona que desacoplar Python con ONNX reduce costos de servidor y mejora latencias en la nube."
      },
      11: {
        title: "6. Resumen de Decisión: Cuándo SÍ vs Cuándo NO Usar Random Forest",
        objective: "Consolidar la matriz de decisión técnica para saber cuándo seleccionarlo y cuándo descartarlo.",
        script: `<p>Para resumir nuestro criterio como profesionales de datos, aquí tenemos la matriz definitiva:</p>
                 <p><strong>Cuándo SÍ usarlo:</strong> En datos tabulares con relaciones no lineales complejas; cuando no quieres perder tiempo escalando o normalizando datos; y cuando buscas un modelo base muy confiable y resistente al sobreajuste.</p>
                 <p><strong>Cuándo NO usarlo:</strong> En series de tiempo con tendencia a futuro donde necesites extrapolar; en dispositivos embebidos o microcontroladores con menos de 2 MB de RAM; y en sistemas que requieran latencias ultraestrictas de microsegundos.</p>`,
        tips: "Lee pausadamente los 3 puntos de cada columna. Esta es la diapositiva que demuestra madurez de criterio técnico."
      },
      12: {
        title: "Conclusiones Finales & Ronda de Preguntas",
        objective: "Recapitular los 4 aprendizajes clave y abrir el espacio de preguntas con el tribunal.",
        script: `<p>En conclusión: Random Forest mantiene el poder del árbol pero cancela su varianza gracias al ensamble; Bagging y Subespacio garantizan la diversidad de Condorcet; SHAP nos permite auditarlo éticamente conociendo su límite de extrapolación; y su paralelismo nativo lo hace un gigante en producción.</p>
                 <p>Muchísimas gracias por su atención. Quedo a su entera disposición para cualquier pregunta o comentario.</p>`,
        tips: "Agradece con una sonrisa y mantén contacto visual con el jurado/docente para iniciar las preguntas."
      }
    };


    /* ---------------------------------------------------------------------- */
    /* NAVIGATION ENGINE                                                      */
    /* ---------------------------------------------------------------------- */
    function initDots() {
      const container = document.getElementById('nav-dots-container');
      container.innerHTML = '';
      for (let i = 1; i <= totalSlides; i++) {
        const dot = document.createElement('button');
        dot.className = `w-2.5 h-2.5 rounded-full transition-all duration-300 ${i === 1 ? 'bg-emerald-400 w-6' : 'bg-slate-700 hover:bg-slate-500'}`;
        dot.title = `Ir a lámina ${i}: ${SLIDE_TITLES[i - 1]}`;
        dot.onclick = () => goToSlide(i);
        container.appendChild(dot);
      }
    }

    function updateNavigationUI() {
      document.getElementById('header-counter-current').textContent = currentSlide;
      document.getElementById('header-slide-topic').textContent = SLIDE_TITLES[currentSlide - 1];

      const progressPercent = (currentSlide / totalSlides) * 100;
      document.getElementById('progress-bar-fill').style.width = `${progressPercent}%`;

      document.getElementById('nav-btn-prev').disabled = (currentSlide === 1);
      document.getElementById('nav-btn-next').disabled = (currentSlide === totalSlides);

      const dots = document.getElementById('nav-dots-container').children;
      for (let i = 0; i < dots.length; i++) {
        if (i + 1 === currentSlide) {
          dots[i].className = 'w-6 h-2.5 rounded-full bg-emerald-400 transition-all duration-300 shadow-md shadow-emerald-400/50';
        } else {
          dots[i].className = 'w-2.5 h-2.5 rounded-full bg-slate-700 hover:bg-slate-500 transition-all duration-300';
        }
      }

      updateSpeakerNotes(currentSlide);
      lucide.createIcons();
    }

    function goToSlide(targetSlide) {
      if (targetSlide < 1 || targetSlide > totalSlides || targetSlide === currentSlide) return;

      const currentElem = document.getElementById(`slide-${currentSlide}`);
      const targetElem = document.getElementById(`slide-${targetSlide}`);

      gsap.to(currentElem, {
        opacity: 0,
        y: -10,
        duration: 0.2,
        ease: 'power2.in',
        onComplete: () => {
          currentElem.classList.remove('active');
          targetElem.classList.add('active');
          window.scrollTo({ top: 0, behavior: 'smooth' });

          gsap.fromTo(targetElem, 
            { opacity: 0, y: 12 }, 
            { opacity: 1, y: 0, duration: 0.3, ease: 'power2.out' }
          );

          currentSlide = targetSlide;
          updateNavigationUI();
        }
      });
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

    function toggleSpeakerNotes() {
      const drawer = document.getElementById('speaker-notes-drawer');
      isSpeakerNotesOpen = !isSpeakerNotesOpen;
      if (isSpeakerNotesOpen) {
        drawer.classList.remove('translate-x-full');
        updateSpeakerNotes(currentSlide);
      } else {
        drawer.classList.add('translate-x-full');
      }
    }

    function updateSpeakerNotes(slideNum) {
      const data = SPEAKER_NOTES[slideNum];
      if (!data) return;

      document.getElementById('drawer-slide-num').textContent = `DIAPOSITIVA ${slideNum} DE 12`;
      document.getElementById('drawer-slide-title').textContent = data.title;
      document.getElementById('drawer-slide-objective').textContent = data.objective;
      document.getElementById('drawer-slide-script').innerHTML = data.script;
      document.getElementById('drawer-slide-tips').textContent = data.tips;
    }

    function toggleFullScreen() {
      if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(err => alert(`Error: ${err.message}`));
      } else {
        if (document.exitFullscreen) {
          document.exitFullscreen();
        }
      }
    }

    function toggleHelpModal() {
      const modal = document.getElementById('modal-help');
      modal.classList.toggle('hidden');
    }

    function closeAllModals() {
      document.getElementById('modal-help').classList.add('hidden');
      if (isSpeakerNotesOpen) {
        toggleSpeakerNotes();
      }
    }

    window.addEventListener('keydown', (e) => {
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT') return;

      if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {
        e.preventDefault();
        nextSlide();
      } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
        e.preventDefault();
        prevSlide();
      } else if (e.key.toLowerCase() === 'f') {
        e.preventDefault();
        toggleFullScreen();
      } else if (e.key === '?' || e.key === 'h' || e.key === 'H') {
        e.preventDefault();
        toggleHelpModal();
      } else if (e.key.toLowerCase() === 'n') {
        e.preventDefault();
        toggleSpeakerNotes();
      } else if (e.key === 'Escape') {
        closeAllModals();
      }
    });

    document.getElementById('btn-fullscreen').addEventListener('click', toggleFullScreen);
    document.getElementById('btn-help').addEventListener('click', toggleHelpModal);

    window.addEventListener('DOMContentLoaded', () => {
      initDots();
      updateNavigationUI();
      lucide.createIcons();
    });
  </script>
</body>
</html>
'''

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Clean theory-first presentation built! Size: {len(html_content)} bytes.")
