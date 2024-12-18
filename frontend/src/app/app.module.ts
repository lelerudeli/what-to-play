import { DEFAULT_CURRENCY_CODE, LOCALE_ID, NgModule } from '@angular/core';

//import { AlertService } from './shared/services/alert.service';
import localePt from '@angular/common/locales/pt';
import { registerLocaleData } from '@angular/common';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app.routes';
import { ToastrModule } from 'ngx-toastr';
import { AlertService } from './shared/services/alert-service/alert.service';
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';
import { MatIconModule } from '@angular/material/icon';
import { SharedModule } from './shared/shared.module';


registerLocaleData(localePt);
@NgModule({
  declarations: [AppComponent],
  bootstrap: [AppComponent],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    ToastrModule.forRoot(
      {
        timeOut: 3000,
        positionClass: 'toast-top-right',
        preventDuplicates: true 
      }
    ),
    HttpClientModule,
    SharedModule,
    MatIconModule
  ],
  providers: [
    AlertService,
    {
      provide: LOCALE_ID,
      useValue: 'pt-BR',
    },
    {
      provide: DEFAULT_CURRENCY_CODE,
      useValue: 'BRL',
    },
    provideAnimationsAsync(),
  ],
})
export class AppModule {}