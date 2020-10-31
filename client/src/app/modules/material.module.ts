import { NgModule } from '@angular/core';

import { MatButtonToggleModule } from '@angular/material/button-toggle';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatIconModule } from '@angular/material/icon';
import { MaterialFileInputModule } from 'ngx-material-file-input';

@NgModule({
    imports: [
        MatButtonToggleModule,
        MatInputModule,
        MatFormFieldModule,
        MatIconModule,
        MaterialFileInputModule
    ],
    exports: [
        MatButtonToggleModule,
        MatInputModule,
        MatFormFieldModule,
        MatIconModule,
        MaterialFileInputModule
    ]
})
export class MaterialModule {}