import type { LinksFunction as RouterLinksFunction } from "react-router";
import type { ReactNode } from "react";

export namespace Route {
  export type LinksFunction = RouterLinksFunction;
  
  export interface ErrorBoundaryProps {
    error: Error;
  }

  export interface LayoutProps {
    children: ReactNode;
  }
}

export type RootType = {
  links: Route.LinksFunction;
};
