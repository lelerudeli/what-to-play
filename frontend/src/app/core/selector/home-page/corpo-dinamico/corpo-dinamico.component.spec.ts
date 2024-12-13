import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CorpoDinamicoComponent } from './corpo-dinamico.component';

describe('CorpoDinamicoComponent', () => {
  let component: CorpoDinamicoComponent;
  let fixture: ComponentFixture<CorpoDinamicoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CorpoDinamicoComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(CorpoDinamicoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
