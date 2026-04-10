/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        bg: '#050908',
        surface: '#080E0A',
        card: '#0B1410',
        card2: '#0F1A14',
        border: '#162018',
        border2: '#1E2E22',
        green: {
          DEFAULT: '#00E896',
          2: '#00C07A',
          3: '#007A50',
        },
        lime: '#AAFF57',
        amber: '#F5A623',
        red: '#FF4757',
        blue: '#00B4FF',
        white: '#EBF5EF',
        muted: '#426052',
        text: '#8AB4A0',
      },
      fontFamily: {
        sans: ['Syne', 'sans-serif'],
        mono: ['JetBrains Mono', 'monospace'],
        serif: ['Lora', 'Georgia', 'serif'],
      },
      borderRadius: {
        card: '12px',
        'card-lg': '18px',
      },
      animation: {
        ticker: 'ticker 40s linear infinite',
        pulse: 'pulse 2s ease infinite',
        blink: 'blink 1s step-end infinite',
        'fade-up': 'fadeUp 0.6s ease forwards',
        'slide-in': 'slideIn 0.4s ease forwards',
      },
      keyframes: {
        ticker: {
          '0%': { transform: 'translateX(0)' },
          '100%': { transform: 'translateX(-50%)' },
        },
        pulse: {
          '0%, 100%': { opacity: '1', transform: 'scale(1)' },
          '50%': { opacity: '0.5', transform: 'scale(1.4)' },
        },
        blink: {
          '0%, 100%': { opacity: '1' },
          '50%': { opacity: '0' },
        },
        fadeUp: {
          from: { opacity: '0', transform: 'translateY(20px)' },
          to: { opacity: '1', transform: 'translateY(0)' },
        },
        slideIn: {
          from: { opacity: '0', transform: 'translateX(-10px)' },
          to: { opacity: '1', transform: 'translateX(0)' },
        },
      },
    },
  },
  plugins: [],
};
