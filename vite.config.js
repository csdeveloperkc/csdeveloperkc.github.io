import { defineConfig } from 'vite';
import tailwindcss from '@tailwindcss/vite';
import { resolve } from 'path';

export default defineConfig({
  plugins: [tailwindcss()],
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        compassion: resolve(__dirname, 'compassion.html'),
        connect: resolve(__dirname, 'connect.html'),
        expect: resolve(__dirname, 'expect.html'),
        grief_share: resolve(__dirname, 'grief-share.html'),
        mens_ministry: resolve(__dirname, 'mens-ministry.html'),
        prayer: resolve(__dirname, 'prayer.html'),
        sermons: resolve(__dirname, 'sermons.html'),
        staff: resolve(__dirname, 'staff.html'),
        womens_ministry: resolve(__dirname, 'womens-ministry.html'),
        give: resolve(__dirname, 'give.html')
      }
    }
  }
});
