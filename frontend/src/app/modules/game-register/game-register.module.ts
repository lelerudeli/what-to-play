import { NgModule } from '@angular/core';

import { GameRegisterComponent } from './game-register.component';
import { SharedModule } from '../../shared/shared.module';
import { CommonModule } from '@angular/common';
import { GameRegisterRoutingModule } from './game-register-routing.module';

@NgModule({
  declarations: [GameRegisterComponent],
  imports: [SharedModule, CommonModule, GameRegisterRoutingModule],
  providers: [],
  bootstrap: [],
})
export class GameRegisterModule {}
