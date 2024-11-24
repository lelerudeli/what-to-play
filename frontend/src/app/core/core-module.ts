import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HeaderComponent } from './header/header.component';
import { CoreRoutingModule } from './core-routing.module';

@NgModule({
  declarations: [
    HeaderComponent
  ],
  imports: [
    CoreRoutingModule,
    CommonModule
  ],
  providers: [],
  bootstrap: []
})
export class CoreModule { }