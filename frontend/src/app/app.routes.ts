import { DEFAULT_CURRENCY_CODE, LOCALE_ID, NgModule } from '@angular/core';

//import { AlertService } from './shared/services/alert.service';
import localePt from '@angular/common/locales/pt';
import { registerLocaleData } from '@angular/common';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { AppRoutingModule } from './app.module';
import { AppComponent } from './app.component';


registerLocaleData(localePt);
@NgModule({
  declarations: [AppComponent],
  bootstrap: [AppComponent],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
  ],
  providers: [
    //AlertService,
    {
      provide: LOCALE_ID,
      useValue: 'pt-BR',
    },
    {
      provide: DEFAULT_CURRENCY_CODE,
      useValue: 'BRL',
    },
  ],
})
export class AppModule {}