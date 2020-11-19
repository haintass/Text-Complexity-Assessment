import { Component, Output, EventEmitter, Input } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { FileTypes } from 'src/app/common/global-constants';

@Component({
  selector: 'file-upload-component',
  templateUrl: './file-upload.component.html',
  styleUrls: ['./file-upload.component.css']
})
export class FileUploadComponent { 
    @Output() onTextProcessing = new EventEmitter<boolean>();

    alertWarningVisibility: boolean = false;
    errorMessage: string;
  
    fileUploadInput: any = null;
    fileToUpload: File = null;
    formData: FormData = null;

    constructor(private http: HttpClient){ }

    handleFileInput(files: FileList, fileUploadInput:any) {
        this.fileToUpload = files.item(0);
        this.fileUploadInput = fileUploadInput;
    }

    uploadFile(){
        if (!this.fileToUpload){
            return;
        }

        if (this.fileToUpload.type != FileTypes.txt) {
            this.alertWarningVisibility = true;
            this.errorMessage = 'errors.incorrectFileExtension';
        }
        else {
            this.formData = new FormData();
            this.formData.append('file', this.fileToUpload, this.fileToUpload.name);

            this.onTextProcessing.emit(true);
          
            this.http.post('/api/uploadFile', this.formData)
            .subscribe(
                response => {
                    this.fileUploadInput.clear();
                    this.fileToUpload = null;

                    this.onTextProcessing.emit(false);
                },
                response => {
                    this.alertWarningVisibility = true;
                    this.errorMessage = response.error.errorType;

                    this.onTextProcessing.emit(false);
                }
            )
        }
    }

    onHideAlert(){
        this.alertWarningVisibility = false;
      }
}