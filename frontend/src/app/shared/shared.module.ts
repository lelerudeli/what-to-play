import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NavigationComponent } from './navigation/navigation.component';
import { AppModule } from '../app.module';
import { MatIconModule } from '@angular/material/icon';

@NgModule({
  declarations: [
    NavigationComponent
  ],
  imports: [
    CommonModule,
    MatIconModule
  ],
  exports: [
    NavigationComponent
  ],
  providers: [],
  bootstrap: []
})
export class SharedModule { }