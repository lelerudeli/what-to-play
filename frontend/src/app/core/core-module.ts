import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HeaderComponent } from './header/header.component';
import { CoreRoutingModule } from './core-routing.module';
import { HomePageComponent } from './home-page/home-page.component';

@NgModule({
  declarations: [
    HeaderComponent,
    HomePageComponent
  ],
  imports: [
    CoreRoutingModule,
    CommonModule
  ],
  providers: [],
  bootstrap: []
})
export class CoreModule { }