import { Component, Input, Output, EventEmitter } from '@angular/core';
import { trigger, style, animate, transition } from '@angular/animations';
  
@Component({
  selector: 'alert-component',
  templateUrl: './alert.component.html',
  styleUrls: ['./alert.component.css'],
  animations: [
    trigger(
      'openClose', 
      [
        transition(':enter', [
          style({ bottom: -40, opacity: 0 }),
          animate('1.2s ease-out', style({ bottom: 5, opacity: 1 }))
        ])
      ]
    )
  ]
})
export class AlertComponent { 
    @Input() message: string;
    @Input() alertType: string = 'alert-warning';

    @Output() onHideAlert = new EventEmitter();

    close() {
        this.onHideAlert.emit();
    }
}