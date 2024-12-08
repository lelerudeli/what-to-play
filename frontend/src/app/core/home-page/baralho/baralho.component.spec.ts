import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BaralhoComponent } from './baralho.component';

describe('BaralhoComponent', () => {
  let component: BaralhoComponent;
  let fixture: ComponentFixture<BaralhoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [BaralhoComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(BaralhoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
