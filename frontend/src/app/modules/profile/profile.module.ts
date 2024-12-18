import { NgModule } from "@angular/core";
import { ProfileComponent } from "./profile.component";
import { SharedModule } from "../../shared/shared.module";
import { CommonModule } from "@angular/common";
import { ProfileRoutingModule } from "./profile-routing.module";
import { MatIconModule } from "@angular/material/icon";



@NgModule({
  declarations: [
    ProfileComponent
  ],
  imports: [
    ProfileRoutingModule,
    MatIconModule,
    SharedModule,
    CommonModule
  ],
  providers: [],
  bootstrap: []
})
export class ProfileModule { }