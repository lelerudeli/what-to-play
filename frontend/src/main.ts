import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';
import { AppModule } from './app/app.routes';

platformBrowserDynamic().bootstrapModule(AppModule)
  .catch(err => console.error(err));