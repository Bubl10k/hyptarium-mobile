import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const rootApi = createApi({
  reducerPath: "rootApi",
  tagTypes: [],
  baseQuery: fetchBaseQuery({
    baseUrl: process.env.API_URL,
  }),
  endpoints: (builder) => ({
    getDefaultRequest: builder.query<string, null>({
      query: () => "/",
    }),
  }),
});

export const { useGetDefaultRequestQuery } = rootApi;
