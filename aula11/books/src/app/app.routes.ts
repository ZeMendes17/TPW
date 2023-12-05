import { Routes } from '@angular/router';
import { AuthorsComponent} from "./authors/authors.component";
import {TopComponent} from "./top/top.component";
import {AuthorDetailsComponent} from "./author-details/author-details.component";

export const routes: Routes = [
  { path: 'authors', component: AuthorsComponent },
  { path: 'top', component: TopComponent },
  { path: 'authordetails/:num', component: AuthorDetailsComponent },
];
