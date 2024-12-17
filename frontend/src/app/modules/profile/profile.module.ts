import { CommonModule } from "@angular/common";
import { ProfileComponent } from "./profile.component";
import { NgModule } from "@angular/core";
import { ProfileRoutingModule } from "./profile-routing.module";
import { SharedModule } from "../../shared/shared.module";



@NgModule({
  declarations: [
    ProfileComponent,
  ],
  imports: [
    SharedModule,
    ProfileRoutingModule,
    CommonModule,
  ],
  providers: [],
  bootstrap: []
})
export class ProfileModule { }