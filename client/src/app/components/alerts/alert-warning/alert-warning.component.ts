import { Component, Input, Output, EventEmitter } from '@angular/core';
  
@Component({
  selector: 'alert-warning-component',
  templateUrl: './alert-warning.component.html',
  styleUrls: ['./alert-warning.component.css']
})
export class AlertWarningComponent { 
    @Input()
    message: string;

    @Output()
    onHideAlert = new EventEmitter();

    close() {
        this.onHideAlert.emit();
    }
}