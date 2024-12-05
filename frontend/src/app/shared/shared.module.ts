import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NavigationComponent } from './navigation/navigation.component';

@NgModule({
  declarations: [
    NavigationComponent
  ],
  imports: [
    CommonModule
  ],
  exports: [
    NavigationComponent
  ],
  providers: [],
  bootstrap: []
})
export class SharedModule { }