import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PapelComponent } from './papel.component';

describe('PapelComponent', () => {
  let component: PapelComponent;
  let fixture: ComponentFixture<PapelComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [PapelComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(PapelComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
