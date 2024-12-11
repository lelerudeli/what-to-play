import { CommonModule } from "@angular/common";
import { AllGamesComponent } from "./all-games.component";
import { NgModule } from "@angular/core";
import { AllGamesRoutingModule } from "./all-games-routing.module";
import { SharedModule } from "../../shared/shared.module";


@NgModule({
  declarations: [
    AllGamesComponent
  ],
  imports: [
    SharedModule,
    AllGamesRoutingModule,
    CommonModule,
  ],
  providers: [],
  bootstrap: []
})
export class AllGamesModule { }